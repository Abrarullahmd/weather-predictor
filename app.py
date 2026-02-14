from flask import Flask, render_template, request, send_file, redirect, url_for
import joblib
import numpy as np
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)

# Load models and label encoder
reg_model = joblib.load('models/weather_regressor.pkl')
cls_model = joblib.load('models/weather_classifier.pkl')
label_encoder = joblib.load('models/label_encoder.pkl')

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data
        input_data = {
            "latitude": float(request.form['latitude']),
            "longitude": float(request.form['longitude']),
            "temperature_celsius": float(request.form['temperature_celsius']),
            "wind_mph": float(request.form['wind_mph']),
            "pressure_mb": float(request.form['pressure_mb']),
            "humidity": float(request.form['humidity']),
        }

        # Convert input to DataFrame to retain feature names
        input_df = pd.DataFrame([input_data])

        # Predict regression values
        prediction_reg = reg_model.predict(input_df)
        predicted_temp, predicted_wind, predicted_humidity, predicted_pressure, predicted_cloud, predicted_precip, predicted_uv = prediction_reg[0]

        # Predict weather condition
        predicted_condition_encoded = cls_model.predict(input_df)[0]
        predicted_condition = label_encoder.inverse_transform([predicted_condition_encoded])[0]

        # Store results
        prediction = {
            "temperature": round(predicted_temp, 2),
            "wind_speed": round(predicted_wind, 2),
            "humidity": round(predicted_humidity, 2),
            "pressure": round(predicted_pressure, 2),
            "cloud_cover": round(predicted_cloud, 2),
            "precipitation": round(predicted_precip, 2),
            "uv_index": round(predicted_uv, 2),
            "weather_condition": predicted_condition
        }

        return render_template('index.html', prediction=prediction)

    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/download_report', methods=['POST'])
def download_report():
    try:
        # Get prediction data from form submission
        prediction_data = request.form

        # Create PDF file
        pdf_path = "static/weather_report.pdf"
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.setFont("Helvetica", 14)

        c.drawString(100, 750, "🌤️ Weather Prediction Report")
        c.line(100, 740, 500, 740)

        y_position = 720
        for key, value in prediction_data.items():
            c.drawString(100, y_position, f"{key.replace('_', ' ').title()}: {value}")
            y_position -= 20

        c.save()

        return send_file(pdf_path, as_attachment=True)

    except Exception as e:
        return f"Error generating PDF: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

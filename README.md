# Weather Predictor

A machine learning-powered weather prediction web application built using **Python** and **Flask**, implementing **Linear Regression** and **Random Forest** models for accurate forecasting.

## Features

- Weather data preprocessing and analysis
- Machine Learning models:
    - Linear Regression
    - Random Forest Classifier

- Web-based interface using Flask
- Real-time weather prediction
- Model comparison capability

## Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn
- **Libraries:** Pandas, NumPy, Matplotlib (if used)
- **Modeling Techniques:** Linear Regression, Random Forest

## Project Structure

```
weather-predictor/
│
├── app.py
├── models/
├── static/
├── templates/
├── dataset/
├── requirements.txt
└── README.md
```

## How It Works

1. Weather dataset is preprocessed and cleaned.
2. Features are selected for model training.
3. Linear Regression and Random Forest models are trained.
4. The best-performing model is used for prediction.
5. Users input parameters via the web interface.
6. The model returns predicted weather conditions.

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Abrarullahmd/weather-predictor.git
cd weather-predictor
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## How to Run the Project

### 1. Activate virtual environment

```bash
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 2. Train the model

```bash
python train_model.py
```

### 3. Run the app

```bash
python app.py
```

### 4. Open (ctrl + click the link in the terminal):

```
http://127.0.0.1:5000/
```

## Future Improvements

- Deploy to cloud (Render / Heroku / AWS)
- Add more ML models (XGBoost, LSTM)
- Improve UI/UX
- Add real-time weather API integration
- Model accuracy comparison dashboard

## Learning Outcomes

- Practical implementation of ML algorithms
- Model evaluation and comparison
- Flask backend integration
- End-to-end ML deployment workflow

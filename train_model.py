import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Import utility functions
from utils import load_and_preprocess_data

# Load and preprocess data
df = load_and_preprocess_data('data/weather_data.csv')

# Select features and targets
features = ['latitude', 'longitude', 'temperature_celsius', 'wind_mph', 'pressure_mb', 'humidity']
X = df[features]

# Target variables
y_regression = df[['temperature_celsius', 'wind_mph', 'humidity', 'pressure_mb', 'cloud', 'precip_mm', 'uv_index']]
y_classification = df['condition_text']

# Encode the weather condition labels
label_encoder = LabelEncoder()
y_classification_encoded = label_encoder.fit_transform(y_classification)

# Split the data
X_train, X_test, y_train_reg, y_test_reg = train_test_split(X, y_regression, test_size=0.2, random_state=42)
X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(X, y_classification_encoded, test_size=0.2, random_state=42)

# Train regression model
reg_model = LinearRegression()
reg_model.fit(X_train, y_train_reg)
y_pred_reg = reg_model.predict(X_test)
mae = mean_absolute_error(y_test_reg, y_pred_reg)
print(f'Mean Absolute Error on Test Data: {mae}')

# Train classification model
cls_model = RandomForestClassifier(n_estimators=100, random_state=42)
cls_model.fit(X_train_cls, y_train_cls)
y_pred_cls = cls_model.predict(X_test_cls)
accuracy = accuracy_score(y_test_cls, y_pred_cls)
print(f'Weather Condition Classification Accuracy: {accuracy}')

# Save models and encoder
joblib.dump(reg_model, 'models/weather_regressor.pkl')
joblib.dump(cls_model, 'models/weather_classifier.pkl')
joblib.dump(label_encoder, 'models/label_encoder.pkl')

print("Models saved successfully!")

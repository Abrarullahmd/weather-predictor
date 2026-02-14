import pandas as pd

def load_and_preprocess_data(filepath):
    """Load and preprocess weather data"""
    df = pd.read_csv(filepath)

    # Select relevant columns
    relevant_columns = [
        'latitude', 'longitude', 'temperature_celsius', 'wind_mph', 'pressure_mb', 'humidity',
        'cloud', 'precip_mm', 'uv_index', 'condition_text'
    ]
    df = df[relevant_columns]

    # Handle missing values
    df = df.dropna()

    return df

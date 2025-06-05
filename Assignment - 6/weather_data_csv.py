import pandas as pd

# Creating the dataframe with sample weather data
data = {
    'Time': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'Temperature': [20 + (x % 10) for x in range(365)],  # Sample temperature data
    'Humidity': [60 + (x % 5) for x in range(365)],  # Sample humidity data
    'WindSpeed': [5 + (x % 3) for x in range(365)],  # Sample wind speed data
    'Rainfall': [0 + (x % 2) for x in range(365)],  # Sample rainfall data
}

df = pd.DataFrame(data)

# Saving the dataframe as a CSV file
df.to_csv('weather_data.csv', index=False)

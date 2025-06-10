# etl/extract.py
# Extract data van een api van temperaturen in amsterdam voor ieder uur 
import requests

def fetch_temperature_data():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.1,  # Amsterdam regio
        "longitude": 5.1,
        "hourly": "temperature_2m",
        "timezone": "Europe/Amsterdam"
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"API-fout: {response.status_code}")
    return response.json()

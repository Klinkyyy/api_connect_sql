# etl/transform.py

import pandas as pd

def transform_temperature_data(raw_json):
    timestamps = raw_json["hourly"]["time"]
    temperaturen = raw_json["hourly"]["temperature_2m"]

    df = pd.DataFrame({
        "tijdstip": pd.to_datetime(timestamps),
        "temperatuur": temperaturen
    })

    return df

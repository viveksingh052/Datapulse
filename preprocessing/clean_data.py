# processing/clean_data.py
import pandas as pd

def clean_data(df):
    df = df[df["TotalConfirmed"] > 1000]  # filter noise
    df["DeathRate"] = (df["TotalDeaths"] / df["TotalConfirmed"]) * 100
    return df

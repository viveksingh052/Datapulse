import pandas as pd

def clean_data(df):
    if df.empty:
        raise ValueError("Input DataFrame is empty!")
    
    # Filter and calculate DeathRate
    df = df[df["TotalConfirmed"] > 1000].copy()
    df["DeathRate"] = (df["TotalDeaths"] / df["TotalConfirmed"]).round(4) * 100  # 4 decimal precision
    
    return df
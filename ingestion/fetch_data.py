# ingestion/fetch_data.py
import pandas as pd
def fetch_covid_data():
    print("⚠️ Using dummy data")
    data = [
        {"Country": "USA", "TotalConfirmed": 5000000, "TotalDeaths": 250000, "TotalRecovered": 3000000},
        {"Country": "India", "TotalConfirmed": 3000000, "TotalDeaths": 50000, "TotalRecovered": 2700000},
        {"Country": "Brazil", "TotalConfirmed": 2000000, "TotalDeaths": 80000, "TotalRecovered": 1800000}
    ]
    return pd.DataFrame(data)

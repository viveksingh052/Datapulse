import pandas as pd
import requests

def fetch_covid_data():
    try:
        url = "https://disease.sh/v3/covid-19/countries"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTP errors
        data = response.json()
        
        # Transform API data to match your schema
        df = pd.DataFrame([{
            "Country": item["country"],
            "TotalConfirmed": item["cases"],
            "TotalDeaths": item["deaths"],
            "TotalRecovered": item["recovered"]
        } for item in data])
        
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"⚠️ API Error: {e}. Using fallback dummy data.")
        # Fallback to dummy data
        return pd.DataFrame([
            {"Country": "USA", "TotalConfirmed": 5000000, "TotalDeaths": 250000, "TotalRecovered": 3000000},
            {"Country": "India", "TotalConfirmed": 3000000, "TotalDeaths": 50000, "TotalRecovered": 2700000}
        ])
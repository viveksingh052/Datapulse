from ingestion.fetch_data import fetch_covid_data
import pandas as pd

def test_fetch_data():
    df = fetch_covid_data()
    assert not df.empty, "DataFrame should not be empty"
    assert "Country" in df.columns, "Missing 'Country' column"
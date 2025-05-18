import pandas as pd
from preprocessing.clean_data import clean_data

def test_clean_data():
    df = pd.DataFrame({
        "TotalConfirmed": [100, 0],
        "TotalDeaths": [10, 0]
    })
    clean = clean_data(df)
    assert "DeathRate" in clean.columns
    assert clean.shape[0] == 1

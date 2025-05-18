import pandas as pd
from datapulse.processing.clean_data import clean_data  # Changed this line

def test_clean_data():
    # Test empty DataFrame
    try:
        clean_data(pd.DataFrame())
        assert False, "Expected ValueError for empty DataFrame"
    except ValueError:
        pass
    
    # Test valid DataFrame
    df = pd.DataFrame({
        "TotalConfirmed": [100, 2000],
        "TotalDeaths": [10, 100]
    })
    cleaned_df = clean_data(df)
    assert "DeathRate" in cleaned_df.columns
    assert cleaned_df.shape[0] == 1  # Only 1 row passes >1000 cases filter
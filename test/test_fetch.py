from ingestion.fetch_data import fetch_data

def test_fetch_data():
    df = fetch_data()
    assert not df.empty

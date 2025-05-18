# run_pipeline.py
from ingestion.fetch_data import fetch_covid_data
from processing.clean_data import clean_data
from storage.save_to_csv import save_to_csv

def run():
    df = fetch_covid_data()
    cleaned_df = clean_data(df)
    save_to_csv(cleaned_df)

if __name__ == "__main__":
    run()

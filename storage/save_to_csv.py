# storage/save_to_csv.py
def save_to_csv(df, path="clean_data.csv"):
    df.to_csv(path, index=False)

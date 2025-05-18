import pandas as pd
import streamlit as st

df = pd.read_csv("clean_data.csv")

st.title("COVID-19 Monitoring Dashboard")
st.dataframe(df[["Country", "TotalConfirmed", "TotalDeaths", "DeathRate"]])

st.bar_chart(df.set_index("Country")["TotalConfirmed"].sort_values(ascending=False).head(10))

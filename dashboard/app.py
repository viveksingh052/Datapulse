import pandas as pd
import streamlit as st
from ingestion.fetch_data import fetch_covid_data
from processing.clean_data import clean_data

# Fetch and clean data
df = fetch_covid_data()
df = clean_data(df)

# Dashboard Title
st.title("COVID-19 Monitoring Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox("Select Country", df["Country"].unique())
min_cases = st.sidebar.slider("Minimum Cases", 1000, int(df["TotalConfirmed"].max()), 1000)

# Filter data
filtered_df = df[
    (df["Country"] == selected_country) & 
    (df["TotalConfirmed"] >= min_cases)
]

# Metrics
st.subheader(f"Metrics for {selected_country}")
col1, col2, col3 = st.columns(3)
col1.metric("Total Confirmed", filtered_df["TotalConfirmed"].sum())
col2.metric("Total Deaths", filtered_df["TotalDeaths"].sum())
col3.metric("Death Rate (%)", f"{filtered_df['DeathRate'].mean():.2f}")

# Visualizations
st.subheader("Top 10 Countries by Cases")
st.bar_chart(df.set_index("Country")["TotalConfirmed"].sort_values(ascending=False).head(10))

# Interactive Plotly Chart
import plotly.express as px
fig = px.scatter(
    df, x="TotalConfirmed", y="TotalDeaths", 
    color="Country", size="DeathRate", 
    hover_name="Country", log_x=True
)
st.plotly_chart(fig)
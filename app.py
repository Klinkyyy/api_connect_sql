# app.py
# stap 1 : maak je venv actief met : cd C:\Users\DASEE\etl_project
# en na stap 1 moet je, je venv activeren met : venv\Scripts\activate
# stap 3 we moeten pip install streamlit (streamlit run app.py)


import streamlit as st
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='config/.env')

# Titel
st.title("🌡️ Temperatuurdashboard")

# Verbind met PostgreSQL
@st.cache_data
def load_data():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    query = "SELECT tijdstip, temperatuur FROM temperaturen ORDER BY tijdstip"
    df = pd.read_sql(query, conn)
    conn.close()
    df["tijdstip"] = pd.to_datetime(df["tijdstip"])
    return df

df = load_data()

# Lijnplot temperatuur per uur
st.subheader("📈 Temperatuur per uur")
st.line_chart(df.set_index("tijdstip"))

# Gemiddelde temperatuur per dag
st.subheader("📊 Gemiddelde temperatuur per dag")
df["datum"] = df["tijdstip"].dt.date
gem_per_dag = df.groupby("datum")["temperatuur"].mean().reset_index()
st.bar_chart(gem_per_dag.set_index("datum"))

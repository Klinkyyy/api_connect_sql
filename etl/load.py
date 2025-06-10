# etl/load.py

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='config/.env')

def connect_db():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

def create_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS temperaturen (
            id SERIAL PRIMARY KEY,
            tijdstip TIMESTAMP UNIQUE,
            temperatuur REAL
        );
    """)
    conn.commit()
    cur.close()

def load_data(conn, df):
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO temperaturen (tijdstip, temperatuur)
            VALUES (%s, %s)
            ON CONFLICT (tijdstip) DO NOTHING;
        """, (row['tijdstip'], row['temperatuur']))
    conn.commit()
    cur.close()

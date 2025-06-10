# main.py

from etl.extract import fetch_temperature_data
from etl.transform import transform_temperature_data
from etl.load import connect_db, create_table, load_data

def run_etl():
    print("🚀 Data ophalen...")
    raw_json = fetch_temperature_data()

    print("🔄 Data transformeren...")
    df = transform_temperature_data(raw_json)

    print("💾 Verbinden met database...")
    conn = connect_db()

    print("🧱 Tabel aanmaken (indien nodig)...")
    create_table(conn)

    print("📥 Data opslaan...")
    load_data(conn, df)

    conn.close()
    print("✅ Klaar!")

if __name__ == "__main__":
    run_etl()

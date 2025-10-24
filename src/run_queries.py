# src/run_queries.py
import pandas as pd
from sqlalchemy import create_engine
from config import DB_URL
from sql_queries import queries

def run_saved_queries():
    engine = create_engine(DB_URL)
    for name, sql in queries.items():
        df = pd.read_sql(sql, engine)
        print(f"\n🔹 {name.upper()}")
        print(df.head())
    print("\n✅ All queries executed successfully.")

if __name__ == "__main__":
    run_saved_queries()

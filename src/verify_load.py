import pandas as pd

DB_URL = "sqlite:///data/herbal_products.db"

def verify_load():
    try:
        df = pd.read_sql("SELECT * FROM herbal_products", DB_URL)
        print(f"✅ Loaded {len(df)} rows from database.")
        print(df.head(5))
    except Exception as e:
        print(f"❌ Error reading from database: {e}")
        



from extract import fetch_products
from transform import transform_products
from load import load_to_db
from verify_load import verify_load
from config import DB_URL
from loguru import logger

# optional: log to file
logger.add("data/etl_log_{time}.log", rotation="1 day", level="INFO")

def main():
    logger.info("🚀 Starting Herbal Products ETL (SQLite)...")

    # 1️⃣ Extract data from API
    df = fetch_products()
    logger.info(f"✅ Extracted {len(df)} records from API.")

    # 2️⃣ Transform / clean data
    df = transform_products(df)
    logger.info(f"✅ Transformed dataset — {len(df)} records ready for load.")

    # 3️⃣ Load data into SQLite
    load_to_db(df, DB_URL)
    logger.info("✅ Data loaded successfully into SQLite database.")

    # 4️⃣ Verify load
    verify_load()

    logger.info("🏁 ETL completed successfully.")

if __name__ == "__main__":
    main()

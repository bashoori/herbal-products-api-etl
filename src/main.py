from extract import fetch_products
from transform import transform_products
from load import load_to_db 
from verify_load import verify_load
from config import DB_URL
from loguru import logger

def main():
    logger.info("Starting Herbal Products ETL...")
    df = fetch_products()
    df = transform_products(df)
    load_to_db(df, DB_URL)
    logger.info("ETL completed successfully.")
    verify_load()

if __name__ == "__main__":
    main()

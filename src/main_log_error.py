from datetime import datetime
import pandas as pd
from loguru import logger

from extract import fetch_products
from transform import transform_products
from load import load_to_db
from verify_load import verify_load
from config import DB_URL

# --- Setup logging ---
logger.add("data/etl_log_{time}.log", rotation="1 day", level="INFO")

def main():
    start_time = datetime.now()
    logger.info("🚀 Starting Herbal Products ETL...")

    # Monitoring dictionary
    etl_status = {
        "start_time": start_time,
        "end_time": None,
        "records_extracted": 0,
        "records_loaded": 0,
        "status": "FAILED",
        "error_message": None,
        "duration_seconds": 0
    }

    try:
        # 1️⃣ Extract
        df = fetch_products()
        etl_status["records_extracted"] = len(df)
        logger.info(f"✅ Extracted {len(df)} records from API.")

        # 2️⃣ Transform
        df = transform_products(df)
        logger.info(f"✅ Transformed dataset — {len(df)} records ready for load.")

        # 3️⃣ Load
        load_to_db(df, DB_URL)
        etl_status["records_loaded"] = len(df)
        logger.info("✅ Data loaded successfully into SQLite database.")

        # 4️⃣ Verify
        verify_load()

        # 5️⃣ Mark as success
        etl_status["status"] = "SUCCESS"

    except Exception as e:
        etl_status["error_message"] = str(e)
        logger.exception("❌ ETL failed due to an unexpected error.")

    finally:
        end_time = datetime.now()
        etl_status["end_time"] = end_time
        etl_status["duration_seconds"] = (end_time - start_time).total_seconds()

        # Log summary
        logger.info(f"📊 ETL Summary: {etl_status}")

        # Save monitoring info
        monitor_path = "data/etl_monitoring.csv"
        df_monitor = pd.DataFrame([etl_status])
        try:
            df_monitor.to_csv(monitor_path, mode="a", header=False, index=False)
            logger.info(f"🗂️ Monitoring log updated: {monitor_path}")
        except Exception as e:
            logger.error(f"⚠️ Could not update monitoring file: {e}")

        logger.info("🏁 ETL process completed.")

if __name__ == "__main__":
    main()

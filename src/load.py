from sqlalchemy import create_engine
from loguru import logger

def load_to_db(df, db_url):
    engine = create_engine(db_url)
    df.to_sql("herbal_products", engine, if_exists="replace", index=False)
    logger.info(f"Loaded {len(df)}")




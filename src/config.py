import os
from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL", "https://ca.naturalfactors.com/collections/specialty-herbalfactors")
DB_URL = os.getenv("DB_URL", "sqlite:///data/herbal_products.db")

#API_URL2 = os.getenv("API_URL", "https://dummyjson.com/products")
#DB_URL2 = os.getenv("DB_URL")

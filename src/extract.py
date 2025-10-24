import requests
import pandas as pd
from config import API_URL

def fetch_products():
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()

    # the JSON has a "products" key containing the list
    df = pd.DataFrame(data["products"])[["id", "title", "price", "category"]]
    df.rename(columns={"title": "name"}, inplace=True)

    print(f"✅ Extracted {len(df)} products from DummyJSON API")
    return df

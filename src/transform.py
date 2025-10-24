import pandas as pd

def transform_products(df):
    # Ensure required columns exist
    if "name" not in df.columns:
        print("⚠️ No name column found — check source format.")
        df["name"] = None
    if "price" not in df.columns:
        print("⚠️ No price column found — adding default None.")
        df["price"] = None

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["source"] = "Mock Herbal API"
    df.dropna(subset=["name"], inplace=True)
    return df

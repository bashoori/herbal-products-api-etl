import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

DB_URL = "sqlite:///data/herbal_products.db"

engine = create_engine(DB_URL)
df = pd.read_sql("SELECT * FROM herbal_products", engine)

st.title("🌿 Herbal Products Dashboard")
st.dataframe(df)

st.bar_chart(df.groupby("category")["price"].mean())

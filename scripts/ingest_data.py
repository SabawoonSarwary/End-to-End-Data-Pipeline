import requests
import pandas as pd
import os
from scripts.utils import logging

def fetch_data():
    """Fetch e-commerce carts from FakeStoreAPI and save raw CSV"""
    url = "https://fakestoreapi.com/carts"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Save raw JSON as CSV
        df = pd.DataFrame(data)
        if not os.path.exists("data"):
            os.makedirs("data")
        df.to_csv("data/raw_sales_data.csv", index=False)
        logging.info(f"Data ingestion completed: {len(df)} records fetched.")
        return df
    except Exception as e:
        logging.error(f"Error in data ingestion: {e}")
        raise

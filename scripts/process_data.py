import pandas as pd
from scripts.utils import logging
import ast

def process_data(input_file="data/raw_sales_data.csv"):
    """Process raw carts data into flat sales data"""
    try:
        df = pd.read_csv(input_file)

        # Convert products column from string to list of dicts
        df['products'] = df['products'].apply(lambda x: ast.literal_eval(x))

        # Explode products into separate rows
        df = df.explode('products').reset_index(drop=True)

        # Extract productId and quantity
        df['product_id'] = df['products'].apply(lambda x: x['productId'])
        df['quantity'] = df['products'].apply(lambda x: x['quantity'])
        df = df.drop(columns=['products'])

        # Rename columns
        df.rename(columns={'id':'order_id','userId':'customer_id'}, inplace=True)

        # Convert date
        df['date'] = pd.to_datetime(df['date'])

        # Add fake price and total price
        df['price_per_item'] = 10.0  # for demo purposes
        df['total_price'] = df['quantity'] * df['price_per_item']

        # Save processed CSV
        df.to_csv("data/processed_sales_data.csv", index=False)
        logging.info(f"Data processing completed: {len(df)} records processed.")
        return df
    except Exception as e:
        logging.error(f"Error in data processing: {e}")
        raise

from scripts.utils import get_db_connection, logging

def load_data(df):
    """Load processed data into SQLite database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Create table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS processed_sales_data (
            order_id INTEGER,
            customer_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            price_per_item REAL,
            total_price REAL,
            date TEXT,
            PRIMARY KEY(order_id, product_id)
        )
        """)
        conn.commit()

        # Insert data
        for _, row in df.iterrows():
            cursor.execute("""
            INSERT OR IGNORE INTO processed_sales_data
            (order_id, customer_id, product_id, quantity, price_per_item, total_price, date)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                int(row['order_id']),
                int(row['customer_id']),
                int(row['product_id']),
                int(row['quantity']),
                float(row['price_per_item']),
                float(row['total_price']),
                str(row['date'])
            ))
        conn.commit()
        cursor.close()
        conn.close()
        logging.info("Data loaded successfully into SQLite database 'ecommerce.db'.")
    except Exception as e:
        logging.error(f"Error in data loading: {e}")
        raise

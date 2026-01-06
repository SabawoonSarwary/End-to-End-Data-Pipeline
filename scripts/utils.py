import sqlite3
import logging
import os

# Create logs folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Setup logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_db_connection(db_name="ecommerce.db"):
    """Create SQLite connection"""
    conn = sqlite3.connect(db_name)
    return conn

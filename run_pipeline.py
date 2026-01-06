from scripts.ingest_data import fetch_data
from scripts.process_data import process_data
from scripts.load_data import load_data

def main():
    print("Starting the E-commerce Sales Data Pipeline...")

    # Step 1: Ingest data
    raw_df = fetch_data()
    print(f"Data ingestion completed: {len(raw_df)} records fetched.")

    # Step 2: Process data
    processed_df = process_data()
    print(f"Data processing completed: {len(processed_df)} records processed.")

    # Step 3: Load into SQLite
    load_data(processed_df)
    print("Data loaded successfully into SQLite database 'ecommerce.db'.")

    print("Pipeline executed successfully! Check 'data/' and 'logs/' folders.")

if __name__ == "__main__":
    main()

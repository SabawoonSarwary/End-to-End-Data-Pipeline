# E-commerce Sales Data Pipeline with Power BI

## Overview
This project is a **complete end-to-end data pipeline**:
- Data ingestion from API
- Data processing with Python/pandas/NumPy
- SQL storage in SQLite
- Visualization with Power BI

## Project Structure

ecommerce_data_pipeline/
├── data/
├── scripts/
├── logs/
├── requirements.txt
└── run_pipeline.py


## Setup Instructions
1. Clone the repository
2. Install dependencies:


pip install -r requirements.txt

3. Run the pipeline:


python run_pipeline.py

4. Open Power BI Desktop and load `data/processed_sales_data.csv` for visualization

## Output
- Raw CSV: `data/raw_sales_data.csv`
- Processed CSV: `data/processed_sales_data.csv`
- SQLite table: `processed_sales_data`
- Power BI dashboard: interactive visualization of sales data

## Next Steps
- Automate pipeline to run daily with Python scheduler
- Enhance transformations with more aggregations
- Add more visualizations in Power BI
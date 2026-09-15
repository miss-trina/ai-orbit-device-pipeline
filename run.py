import os
import logging
from cleaning import DataCleaner
from db_ingestion import DatabaseIngestor

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def main():
    logging.info("Starting AI Orbit Device Pipeline Execution...")
    csv_path = "data/AI_Orbit_Devices_Dataset.csv"
    db_path = "data/ai_orbit.db"
    
    ingestor = DatabaseIngestor(db_path=db_path)
    if os.path.exists(csv_path):
        ingestor.ingest_csv(csv_path)
        logging.info("Pipeline execution completed successfully!")
    else:
        logging.error(f"Dataset CSV not found at {csv_path}")

if __name__ == "__main__":
    main()

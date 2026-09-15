import sqlite3
import csv
import logging

class DatabaseIngestor:
    """Handles automatic SQLite database ingestion for extracted records."""

    def __init__(self, db_path="data/ai_orbit.db"):
        self.db_path = db_path
        self._setup_tables()

    def _setup_tables(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS devices (
                uuid TEXT PRIMARY KEY,
                device_name TEXT NOT NULL,
                manufacturer TEXT,
                category TEXT,
                official_website TEXT,
                official_logo TEXT,
                runs_models TEXT,
                hardware_specs TEXT,
                llm_description TEXT
            )
        """)
        conn.commit()
        conn.close()

    def ingest_csv(self, csv_filepath: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with open(csv_filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            records = [
                (
                   row['id'], row['name'], row['company_manufacturer'],
                    row['category'], row['official_website_url'],
                    row['official_logo_url'], row['runs_models'],
                    row['hardware_type_specs'], row['description']
                ) for row in reader
            ]
            cursor.executemany("""
                INSERT OR REPLACE INTO devices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, records)
        conn.commit()
        conn.close()
        logging.info(f"Successfully ingested {len(records)} records into {self.db_path}")

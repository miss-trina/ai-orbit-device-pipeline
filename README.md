# AI Orbit Ecosystem Data Ingestion Pipeline - Device Module

Production-grade data ingestion pipeline and dataset for the **Device (AI Hardware & Edge Devices)** module of the AI Orbit platform.

## Repository Structure
```text
.
├── data/
│   ├── AI_Orbit_Devices_Dataset.csv
│   └── ai_orbit.db
├── src/
│   ├── cleaning.py
│   └── db_ingestion.py
├── run.py
├── requirements.txt
└── README.md
```

## Setup & Usage

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Pipeline Ingestion**:
   ```bash
   python run.py
   ```

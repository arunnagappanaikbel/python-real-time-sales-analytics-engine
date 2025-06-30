**🔍 Project Objective:**
Analyze real-time performance and delays in public transportation systems using complex, multi-nested JSON from live APIs and CSV files. Perform deep analytics on passenger traffic, route efficiency, congestion levels, average wait time, bus/train delays, and optimization metrics.

**✅ Technologies Used**
- NumPy for statistical analysis.
- pandas for ETL.
- PyYAML for configuration.
- os, logging, json, datetime for utility.
- Optional: Add Pydantic for schema validation later.
- 
🔁 **ETL Workflow**
1. **Data Ingestion**
Read JSON and CSV files.

Validate structure.

Handle corrupted rows or malformed JSON keys.

**2. Transformations using NumPy & pandas**
Normalize nested JSON (e.g. json_normalize).

Time-based aggregations and joins.

Identify average delays per route and per road.

Pivot passenger traffic over time.

Detect congestion patterns using NumPy statistical functions.

Merge traffic and transport data on timestamp + region/road.

**3. Analysis**
Top 5 congested routes vs delay trends.

Correlation between traffic speed and transport delay.

Peak hour analysis using NumPy histogram or percentile.

**4. Output**
Save transformed and analyzed data to processed/ and output/.

Generate summaries in CSV and JSON formats.

## 📂 Repository Structure
```
transport_analytics_project/
├── config/
│   └── config.yaml
├── data/
│   ├── raw/
│   │   ├── traffic/
│   │   └── transport/
│   ├── processed/
│   ├── output/
│   └── logs/
├── src/
│   ├── config_loader.py
│   ├── data_ingestion.py
│   ├── transformer.py
│   ├── analyzer.py
│   ├── file_handler.py
│   ├── logger.py
│   └── main.py
├── test_data/
│   ├── traffic_data.json
│   └── transport_data.csv
├── .env
├── requirements.txt
└── README.md
```
---

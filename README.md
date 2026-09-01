# IoT & System Log Diagnostic Automation Tool

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Database-SQLite](https://img.shields.io/badge/database-SQLite3-lightgrey.svg)](https://www.sqlite.org/)

An automated log parsing and diagnostics system built with Python and SQLite. This tool processes unstructured server/IoT log files using Regular Expressions, converts the parsed data into a structured relational database using Object-Oriented Programming (OOP) principles, and automatically generates summary diagnostic reports using SQL queries.

---

## Key Features

* **Log Parsing:** Utilizes Python Regular Expressions (`re`) to parse timestamp, log level, device ID, and message payloads from raw text log files.
* **Decoupled Architecture (OOP):** Enforces Separation of Concerns by isolating database connections, indexing, and CRUD operations inside a dedicated `DatabaseManager` class (`src/database.py`).
* **Relational Database Management:** Automatically initializes database schemas and indexes in SQLite to optimize query efficiency.
* **Diagnostic Querying:** Executes SQL aggregation queries (`GROUP BY`, `WHERE`) to analyze log level distributions and isolate critical error logs.
* **Automated Reporting:** Exports structured diagnostic summaries directly into text report files.

---

## Project Architecture

```text
log-parser-project/
│── data/
│   └── sample_logs.log         # Sample raw input log file
│── src/
│   ├── database.py             # Data Access Layer (DatabaseManager OOP class)
│   └── log_parser.py           # Application Logic Layer (LogParser OOP class)
│── output/
│   └── diagnostic_report.txt   # Auto-generated diagnostic summary
│── logs.db                     # SQLite database file (generated upon execution)
│── requirements.txt            # Dependency documentation
└── README.md                   # Project documentation

```

---

## How to Run

### Prerequisites

* Python 3.8 or higher installed on your machine.
* No external libraries required (uses built-in `sqlite3`, `re`, and `os` libraries).

### Execution Steps

1. **Clone the repository:**
```bash
git clone [https://github.com/achichiNpikari/log-parser-project.git](https://github.com/achichiNpikari/log-parser-project.git)
cd log-parser-project

```


2. **Run the parser script:**
```bash
python src/log_parser.py

```


3. **Check the outputs:**
* Parsed database: `logs.db`
* Generated report: `output/diagnostic_report.txt`



---

## Sample Diagnostic Output

```text
=== LOG ANALYSIS DIAGNOSTIC REPORT ===

--- Log Level Distribution ---
INFO: 2
WARNING: 1
ERROR: 3

--- Critical Error Details ---
[2026-09-01 10:17:05] Device_01: Connection timeout on port 8080.
[2026-09-01 10:18:22] Device_03: Sensor payload corrupt: ERR_CODE_404.
[2026-09-01 10:20:11] Device_01: Voltage drop detected: ERR_CODE_502.

```

---

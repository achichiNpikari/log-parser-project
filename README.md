\# IoT \& System Log Diagnostic Automation Tool



\[!\[Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

\[!\[Database-SQLite](https://img.shields.io/badge/database-SQLite3-lightgrey.svg)](https://www.sqlite.org/)



An automated log parsing and diagnostics system built with Python and SQLite. This tool processes unstructured server/IoT log files using Regular Expressions, converts the parsed data into a structured relational database using Object-Oriented Programming (OOP) principles, and automatically generates summary diagnostic reports using SQL queries.



\---



\## Key Features



\* \*\*Log Parsing:\*\* Utilizes Python Regular Expressions (`re`) to parse timestamp, log level, device ID, and message payloads from raw text log files.

\* \*\*Decoupled Architecture (OOP):\*\* Enforces Separation of Concerns by isolating database connections, indexing, and CRUD operations inside a dedicated `DatabaseManager` class (`src/database.py`).

\* \*\*Relational Database Management:\*\* Automatically initializes database schemas and indexes in SQLite to optimize query efficiency.

\* \*\*Diagnostic Querying:\*\* Executes SQL aggregation queries (`GROUP BY`, `WHERE`) to analyze log level distributions and isolate critical error logs.

\* \*\*Automated Reporting:\*\* Exports structured diagnostic summaries directly into text report files.



\---



\## Project Architecture



```text

log-parser-project/

│── data/

│   └── sample\_logs.log         # Sample raw input log file

│── src/

│   ├── database.py             # Data Access Layer (DatabaseManager OOP class)

│   └── log\_parser.py           # Application Logic Layer (LogParser OOP class)

│── output/

│   └── diagnostic\_report.txt   # Auto-generated diagnostic summary

│── logs.db                     # SQLite database file (generated upon execution)

│── requirements.txt            # Dependency documentation

└── README.md                   # Project documentation


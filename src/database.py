import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        """建立資料庫連線"""
        return sqlite3.connect(self.db_path)

    def init_db(self):
        """建立資料表與索引"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS system_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    log_level TEXT,
                    device_id TEXT,
                    message TEXT
                )
            """)
            # 建立 Index 優化 SQL 查詢速度
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_log_level ON system_logs(log_level)")
            conn.commit()

    def insert_logs_batch(self, log_entries):
        """批次寫入 parsed log 資料 (Batch Insert)"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.executemany("""
                INSERT INTO system_logs (timestamp, log_level, device_id, message)
                VALUES (?, ?, ?, ?)
            """, log_entries)
            conn.commit()
            return len(log_entries)

    def get_log_level_distribution(self):
        """查詢各 Log Level 數量統計"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT log_level, COUNT(*) FROM system_logs GROUP BY log_level")
            return cursor.fetchall()

    def get_critical_errors(self):
        """查詢所有 ERROR 等級的紀錄"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT timestamp, device_id, message FROM system_logs WHERE log_level = 'ERROR'")
            return cursor.fetchall()
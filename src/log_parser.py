import re
import os
from database import DatabaseManager

class LogParser:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        # 正則表達式：匹配時間、Log等級、設備ID、訊息內容
        self.log_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (\w+) (.+)$")

    def parse_file(self, log_file_path):
        """讀取 Log 文字檔並透過 Regex 進行解析"""
        parsed_entries = []
        with open(log_file_path, "r", encoding="utf-8") as file:
            for line in file:
                match = self.log_pattern.match(line.strip())
                if match:
                    parsed_entries.append(match.groups())

        if parsed_entries:
            count = self.db_manager.insert_logs_batch(parsed_entries)
            print(f"[Success] {count} log entries successfully stored in SQLite database.")
        else:
            print("[Warning] No matching log entries found.")

    def generate_report(self, report_path):
        """調用 DatabaseManager 取得分析數據並輸出報告"""
        level_counts = self.db_manager.get_log_level_distribution()
        error_logs = self.db_manager.get_critical_errors()

        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("=== LOG ANALYSIS DIAGNOSTIC REPORT ===\n\n")
            f.write("--- Log Level Distribution ---\n")
            for level, count in level_counts:
                f.write(f"{level}: {count}\n")
                
            f.write("\n--- Critical Error Details ---\n")
            for ts, dev, msg in error_logs:
                f.write(f"[{ts}] {dev}: {msg}\n")
                
        print(f"[Report] Diagnostic report generated at: {report_path}")

if __name__ == "__main__":
    # 自動取得專案根目錄路徑
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    log_file_path = os.path.join(BASE_DIR, "data", "sample_logs.log")
    db_file_path = os.path.join(BASE_DIR, "logs.db")
    report_file_path = os.path.join(BASE_DIR, "output", "diagnostic_report.txt")

    if not os.path.exists(log_file_path):
        print(f"[Error] 找不到檔案: {log_file_path}")
    else:
        # 1. 初始化資料庫模組
        db_mgr = DatabaseManager(db_file_path)
        db_mgr.init_db()

        # 2. 執行解析與報告生成
        parser = LogParser(db_mgr)
        parser.parse_file(log_file_path)
        parser.generate_report(report_file_path)
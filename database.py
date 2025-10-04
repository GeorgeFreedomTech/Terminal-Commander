import os
import csv
from typing import List, Dict

class CsvDatabase:
    """Handles all direct read/write operations for the CSV file."""

    def __init__(self, file_path: str, headers: List[str]):
        """
        Initializes the database handler.

        Args:
            file_path (str): The full path to the CSV file.
            headers (List[str]): The list of header names for the CSV.
        """
        self._file_path = file_path
        self._headers = headers

    def ensure_db_exists(self) -> None:
        """
        Checks if the database folder and file exist.
        If not, it creates them, including the header row in the file.
        """
        folder = os.path.dirname(self._file_path)
        os.makedirs(folder, exist_ok=True)

        if not os.path.exists(self._file_path):
            with open(self._file_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(self._headers)

    def read_tasks(self) -> List[Dict[str, str]]:
        """Reads all rows from the CSV and returns them as a list of dictionaries."""
        self.ensure_db_exists() # Ensure file exists before reading
        try:
            with open(self._file_path, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except FileNotFoundError:
            return []

    def write_tasks(self, tasks: List[Dict[str, str]]) -> None:
        """Writes a list of task dictionaries to the CSV, overwriting the file."""
        self.ensure_db_exists() # Ensure directory exists before writing
        with open(self._file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self._headers)
            writer.writeheader()
            writer.writerows(tasks)
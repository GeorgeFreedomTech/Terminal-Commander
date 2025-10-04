import os
from typing import List

# Get the directory of the current file
BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))

# Creates a folder for the database
DB_FOLDER: str = os.path.join(BASE_DIR, "commander_db")

# Creates a path to the database file
DB_FILE_PATH: str = os.path.join(DB_FOLDER, "to_do_list.csv")

# Creates a list of headers for the CSV file
CSV_HEADERS: List[str] = ["id", "name", "finished", "created_at"]
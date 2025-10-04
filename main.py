import config
from database import CsvDatabase
from task_manager import TaskManager
from ui import CommandLineUI

def main() -> None:
    """Main function to initialize and run the application."""
    # 1. Initialize the data layer
    db = CsvDatabase(file_path=config.DB_FILE_PATH, headers=config.CSV_HEADERS)

    # 2. Initialize the logic layer (injecting the data layer)
    manager = TaskManager(database=db)

    # 3. Initialize the UI layer (injecting the logic layer)
    ui = CommandLineUI(task_manager=manager)

    # 4. Run the application
    ui.run()

if __name__ == "__main__":
    main()
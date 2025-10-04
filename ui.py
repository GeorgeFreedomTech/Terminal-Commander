from typing import List
from models import Task
from task_manager import TaskManager

class CommandLineUI:
    """Handles the command-line interface for the to-do application."""

    def __init__(self, task_manager: TaskManager):
        """Initializes the UI with a TaskManager."""
        self._task_manager = task_manager
        self._running = True

    def run(self) -> None:
        """Starts the main application loop."""
        print("\n--- Personal TO-DO App ---")
        while self._running:
            self._display_menu()
            choice = input("Enter your choice [1-6]: ")
            self._process_choice(choice)

    def _display_menu(self) -> None:
        """Prints the main menu options to the console."""
        print("\nMenu:")
        print("1. Create/Check DB file")
        print("2. List all tasks")
        print("3. Add a new task")
        print("4. Update a task")
        print("5. Delete a task")
        print("6. Exit")

    def _process_choice(self, choice: str) -> None:
        """Processes the user's menu choice."""
        menu_actions = {
            '1': self._handle_create_db,
            '2': self._handle_list_tasks,
            '3': self._handle_add_task,
            '4': self._handle_update_task,
            '5': self._handle_delete_task,
            '6': self._stop
        }
        action = menu_actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, please try again.")

    def _handle_create_db(self) -> None:
        """Action for creating/checking the database file."""
        self._task_manager.create_db_file()
        print("-> Database file checked/created successfully.")

    def _handle_list_tasks(self) -> None:
        """Action for listing all tasks."""
        print("\n--- Your Tasks ---")
        tasks = self._task_manager.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                status = "✓" if task.finished else "✗"
                created_date = task.created_at.strftime('%Y-%m-%d')
                print(f"[{status}] #{task.task_id}: {task.name} (Created: {created_date})")
        print("------------------")

    def _handle_add_task(self) -> None:
        """Action for adding a new task."""
        name = input("Enter task name: ").strip().capitalize()
        if name:
            task = self._task_manager.add_task(name)
            print(f"-> Task '#{task.task_id}: {task.name}' added successfully.")
        else:
            print("Task name cannot be empty.")

    def _handle_update_task(self) -> None:
        """Action for updating an existing task."""
        try:
            task_id_str = input("Enter the ID of the task to update: ")
            task_id = int(task_id_str)
            
            new_name = input("Enter new name (or press Enter to skip): ").strip().capitalize()
            new_name = new_name if new_name else None

            new_status_str = input("Enter new status (Y/N) (or press Enter to skip): ").strip().upper()
            new_status = None
            if new_status_str == 'Y':
                new_status = True
            elif new_status_str == 'N':
                new_status = False

            updated_task = self._task_manager.update_task(task_id, new_name, new_status)
            if updated_task:
                print(f"-> Task ID: {task_id} updated successfully.")
            else:
                print(f"-> Error: Task with ID: {task_id} not found.")

        except ValueError:
            print("Invalid ID. Please enter a number.")

    def _handle_delete_task(self) -> None:
        """Action for deleting a task."""
        try:
            task_id_str = input("Enter the ID of the task to delete: ")
            task_id = int(task_id_str)
            if self._task_manager.delete_task(task_id):
                print(f"-> Task no. {task_id} deleted successfully.")
            else:
                print(f"-> Error: Task with ID: {task_id} not found.")
        except ValueError:
            print("Invalid ID. Please enter a number.")

    def _stop(self) -> None:
        """Stops the main application loop."""
        self._running = False
        print("Exiting application. Goodbye!")
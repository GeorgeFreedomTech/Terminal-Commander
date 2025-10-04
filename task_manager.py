from datetime import datetime
from typing import List, Optional

from models import Task
from database import CsvDatabase

class TaskManager:
    """Handles the business logic for managing tasks."""

    def __init__(self, database: CsvDatabase):
        """Initializes the manager with a database dependency."""
        self._database = database

    def create_db_file(self) -> None:
        """A wrapper to ensure the database file is created."""
        self._database.ensure_db_exists()

    def get_all_tasks(self) -> List[Task]:
        """Retrieves all tasks and returns them as Task objects."""
        raw_tasks = self._database.read_tasks()
        return [Task.from_dict(task_data) for task_data in raw_tasks]

    def _get_next_id(self) -> int:
        """Calculates the next available ID for a new task."""
        tasks = self.get_all_tasks()
        if not tasks:
            return 1
        return max(task.task_id for task in tasks) + 1

    def add_task(self, name: str) -> Task:
        """Creates a new task, saves it, and returns the created Task object."""
        new_task = Task(
            task_id=self._get_next_id(),
            name=name,
            finished=False,
            created_at=datetime.now()
        )
        
        all_tasks = self.get_all_tasks()
        all_tasks.append(new_task)
        
        self._save_all_tasks(all_tasks)
        return new_task

    def update_task(self, task_id: int, new_name: Optional[str], new_status: Optional[bool]) -> Optional[Task]:
        """Updates a task's name and/or status."""
        tasks = self.get_all_tasks()
        task_to_update = None
        for task in tasks:
            if task.task_id == task_id:
                task_to_update = task
                break
        
        if not task_to_update:
            return None

        if new_name is not None:
            task_to_update.name = new_name
        if new_status is not None:
            task_to_update.finished = new_status
            
        self._save_all_tasks(tasks)
        return task_to_update

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task by its ID. Returns True if successful."""
        tasks = self.get_all_tasks()
        tasks_to_keep = [task for task in tasks if task.task_id != task_id]

        if len(tasks) == len(tasks_to_keep):
            return False # No task was deleted

        self._save_all_tasks(tasks_to_keep)
        return True

    def _save_all_tasks(self, tasks: List[Task]) -> None:
        """Converts Task objects to dicts and writes them to the database."""
        tasks_as_dicts = [task.to_dict() for task in tasks]
        self._database.write_tasks(tasks_as_dicts)
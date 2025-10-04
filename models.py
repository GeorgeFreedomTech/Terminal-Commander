from datetime import datetime
from typing import Dict, Union

class Task:
    """Represents a single to-do task."""

    def __init__(self, task_id: int, name: str, finished: bool, created_at: datetime):
        """
        Initializes a new Task object.

        Args:
            task_id (int): The unique identifier for the task.
            name (str): The description of the task.
            finished (bool): The completion status of the task.
            created_at (datetime): The timestamp when the task was created.
        """
        self.task_id = task_id
        self.name = name
        self.finished = finished
        self.created_at = created_at

    def __repr__(self) -> str:
        """Provides a developer-friendly string representation of the Task object."""
        status = "Done" if self.finished else "Pending"
        return (f"Task(id={self.task_id}, name='{self.name}', status='{status}', "
                f"created='{self.created_at.strftime('%Y-%m-%d %H:%M')}')")

    def to_dict(self) -> Dict[str, Union[int, str, bool]]:
        """Converts the Task object to a dictionary for CSV writing."""
        return {
            "id": self.task_id,
            "name": self.name,
            "finished": "Y" if self.finished else "N",
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def from_dict(data: Dict[str, str]) -> 'Task':
        """Creates a Task object from a dictionary (e.g., a row from a CSV)."""
        return Task(
            task_id=int(data["id"]),
            name=data["name"],
            finished=True if data["finished"] == "Y" else False,
            created_at=datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S")
        )
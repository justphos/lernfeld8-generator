# ----------------
# Automatically generated document
# ----------------
from typing import Callable, List

from generated.entities.tasks_generated import Tasks


class TasksFinder:
    def __init__(self, tasks_factory: Callable[..., Tasks]) -> None:
        self._tasks_factory = tasks_factory
    
    def find_all(self) -> List[Tasks]:
        raise NotImplementedError()


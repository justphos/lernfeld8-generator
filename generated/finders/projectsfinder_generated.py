# ----------------
# Automatically generated document
# ----------------
from typing import Callable, List

from generated.entities.projects_generated import Projects


class ProjectsFinder:
    def __init__(self, projects_factory: Callable[..., Projects]) -> None:
        self._projects_factory = projects_factory
    
    def find_all(self) -> List[Projects]:
        raise NotImplementedError()


# ----------------
# Automatically generated document
# ----------------
from dataclasses import dataclass


@dataclass
class Tasks:
    id: int
    name: str
    priority: int
    status_id: int
    project_id: int
    begin_date: str
    end_date: str

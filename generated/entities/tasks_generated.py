# ----------------
# Automatically generated document
# ----------------
from dataclasses import dataclass


@dataclass
class Tasks:
    id: integer
    name: text
    priority: integer
    status_id: integer
    project_id: integer
    begin_date: text
    end_date: text

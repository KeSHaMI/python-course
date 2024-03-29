from dataclasses import dataclass
from datetime import datetime
from typing import Callable


@dataclass
class Todo:
    id: int
    name: str
    description: str
    is_completed: bool
    created_at: datetime


@dataclass
class Action:
    id: int
    func: Callable
    name: str

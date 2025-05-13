"""
Filename: location.py
Description: File containing the class Location
Author: Tony Le
Created: 10/2/23
"""

from __future__ import annotations
from abc import abstractmethod, ABC
from direction import Direction
from typing import Literal
from task import Task



class Location(ABC):
    """Node-like abstract class representing a location on the map."""
    is_locked = False
    task_complete = False

    def __init__(self, *, connections: dict[Direction, type[Location]], task: Task | None):
        self.connections = connections
        self.task = task

    @abstractmethod
    def action(self) -> Task | None:
        """Location's unique interaction, ex: lights at electrical, or admin task."""


    def get_connection_by_direction(self, direction: Direction) -> type[Location] | Literal[False]:
        """Returns a connected Location via Direction."""
        try:
            return self.connections[direction]
        except KeyError:
            return False

    @classmethod
    def complete(cls) -> bool:
        cls.task_complete = True
        return cls.task_complete

    @classmethod    
    def lock_room(cls) -> bool:
        cls.is_locked = True
        return cls.is_locked
    
    @classmethod
    def unlock_room(cls) -> bool:
        cls.is_locked = False
        return cls.is_locked

    @staticmethod
    def check_task_completions(locations: list[type[Location]]) -> tuple[bool, int, int]:
        """Returns if all tasks in locations are true and number of completed tasks in list."""
        return all(loc.task_complete for loc in locations), [loc.task_complete for loc in locations].count(True), len([loc.task_complete for loc in locations if loc is not None])


    
    def __repr__(self):
        """Returns a repr that prints the class name and a mapping of location's connections to its keys."""
        LOCKED = 'LOCKED'
        COMPLETE = 'Task Complete'
        INCOMPLETE = 'Incomplete'
        return f'{self.__class__.__name__}: {LOCKED + ", " if self.is_locked else ""}{COMPLETE if self.task_complete else INCOMPLETE}. Travel: {[f"{key.name} : {value.__name__ if not value.is_locked else LOCKED} : {COMPLETE if value.task_complete else INCOMPLETE}" for key, value in zip(self.connections.keys(), self.connections.values())]}'


if __name__ == '__main__':
    from map import Dropship
    foo = Dropship()
    print(foo.is_locked)
    print(foo)
    print(foo.lock_room())
    print(foo)
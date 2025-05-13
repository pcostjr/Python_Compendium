"""
Filename: direction.py
Description: File containing the enum Direction.
Author: Tony Le
Created: 10/2/23
"""

from __future__ import annotations
from enum import Enum


class Direction(Enum):
    """Enum containing string constants representing the cardinal and ordinal directions."""
    NORTH = 'n'
    SOUTH = 's'
    WEST = 'w'
    EAST = 'e'
    NORTHWEST = 'nw'
    SOUTHWEST = 'sw'
    NORTHEAST = 'ne'
    SOUTHEAST = 'se'
    

    @classmethod
    def get_values(cls):
        """Returns a tuple containing each enum members' value."""
        return tuple(c.value for c in cls)
        # Generated tuple rather than list comprehension to allow tuple to be cached
    
    @classmethod
    def get_names(cls, *, lower: bool = False):
        """Returns a tuple containing each enum members' name, takes a kwarg boolean to determine whether to return names in lowercase."""
        if lower:
            return tuple(c.name.lower() for c in cls)
        else:
            return tuple(c.name for c in cls)
        # Generated tuple rather than list comprehension to allow tuple to be cached

    @staticmethod
    def str_to_direction(direction) -> Direction:
        if direction in Direction.get_names(lower=True):
            direction = Direction[direction.upper()] # type: ignore
        if direction in Direction.get_values():
            direction = Direction(direction)
        return direction



if __name__ == '__main__':
    print(Direction.get_names(lower=True))
    print(Direction.get_values())
    print(Direction.str_to_direction('s'))

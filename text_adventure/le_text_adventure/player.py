"""
Filename: player.py
Description: File containing the class Player.
Author: Tony Le
Created: 10/2/23
"""

from dataclasses import dataclass
from location import Location
from direction import Direction


@dataclass
class Player:
    """Class for Player and all NPCs."""
    current_location: type[Location]

    def movement(self, direction: Direction) -> bool:
        """
        Move to another Location on the map if valid.\n
        Takes a Direction and returns location.
        """
        get_connection: type[Location] = self.current_location.get_connection_by_direction(direction) # type: ignore
        if not get_connection:
            if not Player in self.__class__.__bases__ and not NPC in self.__class__.__bases__: # Conditional that checks strictly for the parent class and never for subclases.
                if self.current_location.is_locked:
                    return False
            return True
        self.set_location(get_connection()) # type: ignore
        return True


    def set_location(self, other_location: type[Location]):
        self.current_location = other_location
        return
    
class NPC(Player):
    """Class for NPCs."""

if __name__ == '__main__':
    from map import Dropship
    foo = Player(Dropship()) # type: ignore
    print(foo)
    print(foo.movement(direction=Direction.SOUTH))
    print(foo)
    bar = NPC(Dropship()) # type: ignore
    print(bar)
    print(isinstance(bar, NPC))
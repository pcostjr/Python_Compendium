"""
Filename: impostors.py
Description: File containing the impostor class.
Author: Tony Le
Created: 10/20/23
"""
from player import Player, NPC
from dataclasses import dataclass
from random import randint, choice
from direction import Direction

@dataclass
class Impostor(NPC):
    """Class inheriting from NPC that represents an enemy."""
    def kill_player(self, player: Player) -> bool:
        """Kill player if player is in the same location."""
        if player.current_location == self.current_location:
            return True
        else:
            return False
    
    def sabotage(self, player: Player):
        """Lock parts of the map."""
        sabotage_options = randint(1, 2)
        if sabotage_options == 1:
            player.current_location.lock_room()
        elif sabotage_options == 2:
            player.current_location.get_connection_by_direction(choice(list(Direction))) # type: ignore
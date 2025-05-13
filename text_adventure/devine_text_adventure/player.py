from room import Room
from inventory import Inventory


class Player:
    def __init__(self, room: Room):
        # takes an initial room and runs the set command
        self.set_current_room(room)
        #create an inventory instance
        self.inv = Inventory([])

    def set_current_room(self, room: Room):
        #checks if the room is locked, if it we raise a perm error
        if room.locked:
            raise PermissionError("Room Locked")
        self.current_room = room

    # returns the room the player is currently in
    def get_current_room(self):
        return self.current_room

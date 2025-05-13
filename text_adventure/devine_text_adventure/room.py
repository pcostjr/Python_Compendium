from constants import DIRECTIONS, ROOM_TYPES
from inventory import Inventory


class Room:
    #creates a room with a name, description, coord pair, inventory, locked bool
    def __init__(self, name: str, description: str, x: int, y: int):
        self.name = name
        self.description = description
        self.coord = (x, y)
        self.inv = Inventory([])
        self.locked = False


        #sets the 4 directions room as None initially
        for dir in DIRECTIONS:
            setattr(self, dir, None)

    #if the surrounding rooms exist we print out their names and
    #the relative direction
    def __str__(self):
        adj_rooms = []
        for direction in DIRECTIONS:
            if (adj_room := self.get_room(direction)):
                room_name = adj_room.get_name()

                adj_rooms.append(f'{direction.capitalize()}: {room_name}')

        return "\n".join(adj_rooms)

    #add a room based off direction
    def add_room(self, direction, room):
        #makes sure we enter a valid direction
        if not direction in DIRECTIONS:
            raise TypeError("Invalid Direction")

        setattr(self, direction, room)

    #gets a room based off direction
    def get_room(self, direction):
        #makes sure we enter a valid direction
        if not direction in DIRECTIONS:
            raise TypeError("Invalid Direction")

        return getattr(self, direction)

    #!!!!!!!FOR DEV PURPOSES ONLY!!!!!!!!!!!!
    # def get_type(self) -> int:
    #     if self.name == "Start":
    #         return "X"
    #     if self.name == "End":
    #         return "Y"
    #     if self.locked:
    #         return "🔒"
    #     try:
    #         if self.inv.get_item("RedKey"):
    #             return "K"
    #     except ValueError:
    #         print("No red key")

    #     return ROOM_TYPES.index(self.name)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # self.name wrapping method
    def get_name(self) -> str:
        return self.name

    # self.description wrapping method
    def get_description(self) -> str:
        return self.description

    # sets locked state to True and tells what key is required to unlock it
    def lock_room(self, required_key):
        self.locked = True
        self.required_key = required_key
        return self

    #unlocks room
    def unlock_room(self, key):
        #checks if room room is already unlocked
        if not self.locked:
            print("Room is not locked!")

        #checks if the current key is provided
        elif key != self.required_key:
            print('Invalid Key')
        
        #else unlock room
        else:
            self.locked = False

        return self

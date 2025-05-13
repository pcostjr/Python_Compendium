from constants import DIRECTIONS, ROOM_TYPES
from random import randint
from map import Map
from player import Player
from items import Item

#generates an arbitrarily sized maze
m = Map(4, 4)

# creates room objects at each spot in the grid
m.populate_rooms()

# iterates through each room and connects them together
m.sync_rooms()

# creates the player at the starting room of the maze
p = Player(m.get_room(m.start[1], m.start[0]))

#create an item named RedKey
keyA = Item("RedKey")

#generates the locked room and key locations based off an inital object
m.generate_locked_room_and_keys(keyA)

#Starting Game message
print("Your objective is to navigate to the Ending room!")
print("Use \"help\" for more info!")

while True:
    #if the name of the players current room is end then they have won
    if p.get_current_room().get_name() == "End":
        print("Congratulations! You escaped")
        quit()

    #strips extra spaces and splits user input based off of spaces
    cmd = input("> ").strip().split(" ")

    #prints out list of commands that are valid and their syntax
    if cmd[0] == "help":
        print("north, south, east, west: travel in that direction if its valid!")
        print("look: gives details about items in room and surrounding rooms")
        print("huh?: displays current room")
        print("inv: displays players inventory")
        print("pickup <item>: picks up a valid item *CAPS MATTER*")
        print(
            "use <item> on <direction>: uses a valid item on a room in the given direction!")

    #checks for all commands that are a valid direction
    elif cmd[0] in DIRECTIONS:
        #checks if the adj_room variable is not none
        #adj_room is set to the players current room then the direction the user specified to move
        if (adj_room := p.get_current_room().get_room(cmd[0])):
            #attempts to set the players room
            #if it can't its because the room is locked
            try:
                p.set_current_room(adj_room)
            except PermissionError:
                print("Room is currently locked, find the key!")
        #if the adj_room is None then their is a wall there
        else:
            print("You bumped into a wall!")

    #prints the current rooms surrounding rooms and inventory
    elif cmd[0] == "look":
        print("\nAdjacent Rooms:\n", p.get_current_room())
        print("\nItems:\n", p.get_current_room().inv)

    #prints room name and description
    elif cmd[0] == 'huh?':
        print(
            f'{p.get_current_room().get_name()}: {p.get_current_room().get_description()}')

    #prints players inventory
    elif cmd[0] == 'inv':
        print(p.inv)

    elif cmd[0] == "pickup":
        # removes item from room and adds it to players inventory
        #try except block for error catching
        try:
            item = p.get_current_room().inv.remove_item(cmd[1])
            p.inv.add_item(item)

        except IndexError:
            print("You did not specify an item")

        except ValueError:
            print("Item not found")

    #use <item> on <direction>
    #checks if "use" and "on" are in the command
    elif cmd[0] == "use" and cmd[2] == "on":

        #attempts to get an inputted item from the users inventory
        #try except block for error catching
        try:
            item = p.inv.get_item(cmd[1])


            #checks if the 4th arguments is a valid direction
            if cmd[3] in DIRECTIONS:
                #gets the room based off the direction the user specified relative to the players current room
                if (adj_room := p.get_current_room().get_room(cmd[3])):
                    #attempts to unlock room
                    adj_room.unlock_room(item)
                    #if room is not locked then the room is successfully unlocked
                    if adj_room.locked == False:
                        print("Room Unlocked!")

                #if adj_room is None then there was a wall
                else:
                    print("There is no room at the provided direction!")
            else:
                print("Invalid Direction Provided")

        except IndexError:
            print("You did not specify an item")
        except ValueError:
            print("You do not have this item")

    #!!DEVELOPMENT COMMANDS!!!!
    # elif cmd[0] == 'devmap':
    #     print(m)
    # elif cmd[0] == 'devmove':
    #     r = m.get_room(int(cmd[1]), int(cmd[2]))
    #     print(r.get_name())
    #     p.set_current_room(r)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!

    print()

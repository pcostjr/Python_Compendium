from room import Room
from constants import DIRECTIONS, ROOM_TYPES

from random import choice

from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.solve.BacktrackingSolver import BacktrackingSolver


# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

class Map:

    def __init__(self, h, w):
        #generates a maze, solutions to the maze, and starts and ending to the maze use the Prims algorithm
        self.maze = Maze()

        self.maze.generator = Prims(h, w)
        self.maze.generate()

        self.maze.solver = BacktrackingSolver()
        self.maze.generate_entrances()
        self.maze.solve()

        self.start = self.maze.start
        self.end = self.maze.end

    #get wrapper for self.grid
    def get_grid(self): return self.grid

    #get wrapper for self.grid at a specific x, y
    def get_room(self, x, y): return self.grid[y][x]

    #adds rooms to the spots in the grid based off of the text generated maze
    def populate_rooms(self):
        grid = []

        #iterates over the grid columns with an index
        for y, row in enumerate(self.maze.grid):
            #adds a blank column to grid
            grid.append([])

            #iterates over the cells in the row with an index
            for x, cell in enumerate(row):
                #if the cell is a 0 then it is a room and we generate a random room from our valid room types
                if cell == 0:
                    grid[y].append(Room(choice(ROOM_TYPES), "", x, y))

                #if the cell is a 1 then it is a wall and doesn't need a type
                elif cell == 1:
                    grid[y].append(None)

        #overwrites any previously created rooms/wall for the starting and ending rooms
        grid[self.start[0]][self.start[1]] = Room(
            "Start", "Room you begin in!", *self.start)
        grid[self.end[0]][self.end[1]] = Room(
            "End", "Objective Room", *self.end)

        self.grid = grid

    #iterates over all create rooms and connects them together if needed
    def sync_rooms(self):
        #iterates over the grid columns with an index
        for y, row in enumerate(self.get_grid()):
            #iterates over the row cells with an index
            for x, cell in enumerate(row):
                #if the cell is None, its a wall and we can skip
                if not cell:
                    continue

                #we iterate over the directions and how they exist relative based off of x, y values
                #in respect to the current room
                for dir in [(1, 0, "east"), (-1, 0, "west"), (0, 1, "north"), (0, -1, "south")]:
                    #incase we are at the edge of the maze we might get an IndexError that we can just skip
                    try:
                        #checks if the adjacent room isn't a wall and creates a variable called adj_room
                        #using the walrus operator
                        if (adj_room := self.grid[y + dir[1]][x + dir[0]]):
                            #creates a connection
                            self.grid[y][x].add_room(dir[2], adj_room)
                    except IndexError:
                        continue

        #returns grid full of connected rooms (Valid Graph)
        return self.get_grid()

    #generates a locked room that always interferes with the players
    #ability to complete the maze
    #also generates a key at the first valid spot away from the player
    def generate_locked_room_and_keys(self, key):
        #vital_rooms are rooms that lead to the exit
        vital_rooms = []
        #defines the first room that has 3 connecting rooms allowing for a new path
        first_branch_room = None

        #iterates over the first valid solution to the maze with an index
        for idx, coord in enumerate(self.maze.solutions[0]):
            #gets the room instance form its coords
            r = self.get_room(coord[1], coord[0])

            #iterates over each direction to see if there is a room
            #if it is return an arbitrary value
            #then we count the number of values which equals number of connections
            num_of_connections = len(
                [dir for dir in DIRECTIONS if r.get_room(dir)])

            #if number of connections is 2 or more it is still a required part of the solution path
            if num_of_connections >= 2:
                vital_rooms.append(r)

            #if first_branch_room still hasn't been set and 
            #the number of connections to the room is more than 2
            #then we set first_branch_room to the current room
            if num_of_connections > 2 and first_branch_room == None:
                first_branch_room = idx

        #makes sure we can only choose from rooms after the first "branch off"
        vital_rooms = vital_rooms[first_branch_room+1:]

        #we then select a random room to lock
        locked_room = choice(vital_rooms)

        #when locking the room we provide the only valid item to unlock it
        locked_room.lock_room(key)

        #gets the instance of the starting room from its coords
        start_room = self.get_room(self.start[1], self.start[0])

        #a dictionary that stores where we have visited
        #and the distance from the origin
        visited = dict()

        #attempts to find furthest away room from a node without crossing locked rooms
        def check_room(room, y):
            #iterates through all valid directions
            for dir in DIRECTIONS:
                #if the room exists at the specified direction
                if (branch_room := room.get_room(dir)):
                    #checks if the room isn't locked and it has not been visited
                    if not branch_room.coord in visited and not branch_room.locked:
                        #adds that we are now visiting room
                        visited[branch_room.coord] = y
                        #reruns check with the current branch as the new start node
                        check_room(branch_room, y+1)

        #inits check
        check_room(start_room, 0)
        
        #converts dictionary to list of keys and values
        #then sortes the values in descending order based of its value
        #then we select the first entry and then we select the key which is its coord
        furthest_room_coord = sorted(visited.items(), reverse=True, key=lambda x: x[1])[0][0]

        #we get the room instance based off this coord
        furthest_room = self.get_room(*furthest_room_coord)

        #we then store the key in this room
        furthest_room.inv.add_item(key)

    #!!!!!!!!!!!!!!!!!!!!!!DEV ONLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #prints out the map based off room type
    # def __str__(self):
    #     return "\n".join(
    #         [" ".join(
    #             [
    #                 (" " if not j else str(j.get_type())) for j in i
    #             ]) for i in self.grid
    #          ]
    #     )
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

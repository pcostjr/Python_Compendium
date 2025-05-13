"""
Filename: map.py
Description: File containing the classes that represent the map of the game.
Author: Tony Le
Created: 10/4/23
"""

from player import Player
from location import Location
from direction import Direction as dir
from task import Task

SOUTH = dir.SOUTH
WEST = dir.WEST
EAST = dir.EAST
NORTH = dir.NORTH
SOUTHWEST = dir.SOUTHWEST
SOUTHEAST = dir.SOUTHEAST
NORTHEAST = dir.NORTHEAST
NORTHWEST = dir.NORTHWEST


def get_locations() -> list[type[Location]]:
    return [Dropship, Electrical, Outside_North, Outside_South, Outside_West, Admin, 
            Oxygen, Weapons, Storage, Decontamination_East, Decontamination_West, 
            Med_Bay, Lava_Pit, Communications, Laboratory, Nuclear_East, Nuclear_West]


class Dropship(Location):
    def __init__(self):
        super().__init__(connections={SOUTH: Outside_North,
                                    WEST: Laboratory,
                                    NORTHWEST: Nuclear_West,
                                    EAST: Electrical,
                                    NORTHEAST: Nuclear_East},
                        task=Task('Keys', 'Insert keys into dropship.'))

    def action(self):
        return self.task

class Electrical(Location):
    def __init__(self):
        super().__init__(connections={NORTHWEST: Dropship,
                                    EAST: Outside_North,
                                    WEST: Cameras,
                                    SOUTH: Oxygen},
                        task=Task('Lights', 'Turn the lights back on.'))

    def action(self):
        return self.task

class Outside_North(Location):
    def __init__(self):
        super().__init__(connections={NORTH: Dropship,
                                    EAST: Storage,
                                    WEST: Outside_West,
                                    SOUTH: Outside_South,
                                    NORTHEAST: Electrical},
                        task=Task('Node', 'Fix weather node.'))

    def action(self):
        return self.task

class Outside_West(Location):
    def __init__(self):
        super().__init__(connections={SOUTH: Outside_South,
                                    EAST: Outside_North,
                                    NORTH: Outside_North,
                                    NORTHEAST: Outside_North},
                        task=Task('Node', 'Fix weather node.'))
    
    
    def action(self):
        return self.task

class Outside_South(Location):
    task_complete = True
    def __init__(self):
        super().__init__(connections={SOUTH: Weapons,
                                    NORTH: Communications,
                                    NORTHEAST: Outside_North,
                                    NORTHWEST: Outside_West,
                                    EAST: Admin,
                                    WEST: Oxygen},
                        task=None)
    
    def action(self):
        return self.task

class Admin(Location):
    task_complete = True
    def __init__(self):
        super().__init__(connections={SOUTH: Decontamination_East,
                                    EAST: Lava_Pit,
                                    WEST: Outside_South},
                        task=None)
    
    def action(self):
        return self.task

class Oxygen(Location):
    def __init__(self):
        super().__init__(connections={WEST: Outside_South,
                                    NORTHEAST: Cameras,
                                    NORTHWEST: Electrical},
                        task=Task('Monitor', 'Monitor the tree\'s vitals.'))
    
    
    def action(self):
        return self.task

class Weapons(Location):
    def __init__(self):
        super().__init__(connections={NORTH: Outside_South},
                        task=Task('Asteroids', 'Blast asteroids in the atmosphere.'))
    
    
    def action(self):
        return self.task

class Storage(Location):
    def __init__(self):
        super().__init__(connections={WEST: Outside_North},
                        task=Task('Gas', 'Fill gas canister.'))
    
    
    def action(self):
        return self.task

class Decontamination_West(Location):
    def __init__(self):
        super().__init__(connections={EAST: Decontamination_East,
                                    WEST: Admin},
                        task=Task('Artifacts', 'Store artifacts securely.'))
    
    
    def action(self):
        return self.task

class Decontamination_East(Location):
    def __init__(self):
        super().__init__(connections={WEST: Decontamination_West,
                                    NORTH: Med_Bay},
                        task=Task('Wires', 'Fix wiring.'))
    
    
    def action(self):
        return self.task

class Med_Bay(Location):
    def __init__(self):
        super().__init__(connections={SOUTH: Decontamination_West,
                                    WEST: Laboratory},
                        task=Task('Scan', 'Scan for impostors!'))
    
    
    def action(self):
        return self.task

class Lava_Pit(Location):
    def __init__(self):
        super().__init__(connections={SOUTHWEST: Admin,
                                    NORTHWEST: Laboratory},
                        task=Task('Temperature', 'Record the lava\'s temperature'))
    
    
    def action(self):
        return self.task

class Cameras(Location):
    def __init__(self):
        super().__init__(connections={EAST: Electrical,
                                    SOUTH: Oxygen},
                        task=Task('Cameras', 'Look for impostors!'))
    
    
    def action(self):
        return self.task

class Communications(Location):
    def __init__(self):
        super().__init__(connections={SOUTH: Outside_South},
                        task=Task('Upload', 'Upload data.'))
    
    
    def action(self):
        return self.task

class Laboratory(Location):
    def __init__(self):
        super().__init__(connections={NORTHWEST: Dropship,
                                    EAST: Med_Bay,
                                    SOUTHEAST: Lava_Pit,
                                    SOUTH: Lava_Pit,
                                    NORTH: Nuclear_West,
                                    SOUTHWEST: Outside_North},
                        task=Task('Telescope', 'Look for astronomical objects.'))
    
    
    def action(self):
        return self.task

class Nuclear_West(Location):
    def __init__(self):
        super().__init__(connections={SOUTHEAST: Laboratory,
                                    WEST: Dropship,
                                    SOUTHWEST: Outside_North},
                        task=Task('Nuclear', 'Stop the nuclear meltdown!'))
    
    
    def action(self):
        return self.task

class Nuclear_East(Location):
    def __init__(self):
        super().__init__(connections={EAST: Dropship,
                                    SOUTHEAST: Outside_North},
                        task=Task('Nuclear', 'Stop the nuclear meltdown!'))

    
    def action(self):
        return self.task

if __name__ == '__main__':
    print(get_locations())
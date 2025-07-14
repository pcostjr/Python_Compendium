"""
Filename: sqlite_main.py
Description: Main file to be run for text_adventure.
Author: Tony Le
Created: 10/2/23
"""

from player import Player, NPC
from impostors import Impostor
import map
from location import Location
from direction import Direction
from unlock_puzzle import unlock_room
from task import Task
from tqdm import tqdm
from time import sleep
from random import randint


def boot_game() -> tuple[Player, list[NPC | Impostor]]:
    player = Player(map.Dropship()) # type: ignore
    NPCS: list[NPC | Impostor] = [NPC(map.get_locations()[randint(0, len(map.get_locations()) - 1)]()) for _ in range(7)] # type: ignore
    NPCS.extend(([Impostor(map.get_locations()[randint(0, len(map.get_locations()) - 1)]()) for _ in range(2)])) # type: ignore
    # List of NPCs and Impostors, randomly placed throughout the map.
    # 2 Impostors and 7 NPCs.

    print(f'Welcome to Polus. You have arrived at the Dropship.\n')
    print(f'Complete every task to escape the impostors!\n')
    print(f'Type "HELP" for a list of commands.\n')
    print(player.current_location)
    return player, NPCS


def game_loop(player: Player, NPCS: list[NPC | Impostor]):
    while True:
        print()
        user_input = input('Commands: ').lower()
        print()
        if return_value := command(user_input, player):
            print('Congratulations! You have escaped Polus!')
            quit('Game complete.')
        elif return_value is None: # Player moved or did some non-game action, like the help command.
            continue
        elif return_value is False: # Player did task or unlocked door.
            npc_locations = npc_actions(NPCS, player)
        same_location_npcs = [loc for loc in npc_locations if loc.__class__ == player.current_location.__class__]
        print(f'There are {len(npc_locations)} crewmates in Polus.')
        print(f'There are {len(same_location_npcs)} crewmates in your current location.')



def npc_actions(NPCS: list[NPC | Impostor], player: Player) -> list[type[Location]]:
    npc_locations: list[type[Location]] = []
    for npc in NPCS:
        npc.movement(Direction[Direction.get_names()[randint(0, len(Direction.get_names())-1)]].name) # type: ignore
        npc_locations.append(npc.current_location)        
        # Random movement.
        if isinstance(npc, Impostor):
            impostor_action = randint(1, 4)
            if impostor_action == 1:
                if npc.kill_player(player):
                    print('You were slain by the impostors!')
                    quit('Game over.')
            elif impostor_action == 2:
                npc.sabotage(player)
    return npc_locations


def command(commands: str, player: Player) -> bool | None:
    """Gameplay function."""
    print(commands)
    direction_check = lambda direction: direction in Direction.get_values() or direction in Direction.get_names(lower=True)
    # Function to check if a given string is some direction or name of direction

    match commands.split():
        case ['self' | 'current' | 'location']:
            print(player.current_location)
            return None

        case ['go' | 'travel' , direction] | [direction] if direction_check(direction):
            direction = Direction.str_to_direction(direction)

            if other_location := player.current_location.get_connection_by_direction(direction): # type: ignore
                if other_location.is_locked:
                    print('This location is locked.')
                    return None
                else:
                    movement_result = player.movement(direction)
                    if movement_result is False:
                        print('Your current location is locked. Unlock the room to move.')
                        return None
                    else:
                        print(player.current_location)
            else:
                print('This direction has no location.')
                return None
            return False

        case ['do', 'task'] | ['task']:
            task: Task | None = player.current_location.action() # type: ignore
            if not task:
                print('This location has no task.')
                return None
            if player.current_location.task_complete:
                print('This task has already been completed.')
                return None
            print(f'{task.name}: {task.description}')
            for _ in tqdm(range(5), desc='Completing task...'):
                sleep(0.5)
            print(f'{task.name}: Task complete.')
            player.current_location.complete()
            if player.current_location.check_task_completions(map.get_locations())[0]: 
                return True
            else:
                return False

        case ['remaining'] | ['rem']:
            locations = map.get_locations()
            print(f'{player.current_location.check_task_completions(locations)}')
            return None

        case ['unlock', direction] if direction_check(direction):
            direction = Direction.str_to_direction(direction)
            if other := player.current_location.get_connection_by_direction(direction):
                unlock_room(other)
            else:
                print('This direction has no location.')
            return None
        case ['unlock']:
            unlock_room(player.current_location)
            return None

        case ['commands' | 'help']:
            print("""
                SELF | CURRENT | LOCATION
                    : Print your current location.
                
                {GO | TRAVEL} [direction] | [direction]
                    : Travel to another location via given direction.
                
                DO TASK | TASK
                    : Do location's task, if possible.
                
                REMAINING | REM
                    : Check number of remaining tasks.
                
                UNLOCK
                    : If room is locked, prompts the unlock puzzle for the current room.
                
                (Q)UIT | EXIT | CLOSE
                    : Exit game.
                """)
            return None
        case ['quit' | 'exit' | 'close' | 'q']:
            # Kaboom
            quit('Player manually exited.')
        case _:
            print("I don't understand this instruction.")
            return None



if __name__ == '__main__':
    start = boot_game()
    game_loop(start[0], start[1])
"""
Filename: unlock_puzzle.py
Description: A file containing the unlock puzzle in text_adventure.
Author: Tony Le
Created: 10/13/23
"""

from random import randint
import re
from location import Location

def make_puzzle():
    """Creates the locked door."""
    door_lock_matrix = [[[True], [True], [True], [True]], 
                        [[True], [True], [True], [True]]] # 2x4 matrix representing a locked door
    
    for row in door_lock_matrix:
        # Add default unlocks.
        for _ in range(randint(1, 2)):
            row[randint(0, 3)][0] = False
    return door_lock_matrix

def digit_match(str) -> bool:
    return bool(re.match(pattern='\d', string=str)) # type: ignore

def solve(puzzle=None):
    """User interface to solve puzzle."""
    if not puzzle:
        puzzle = make_puzzle()
    unsolved = True

    print(f'Unlocked sections are False. Locked sections are True.')
    print(f'To unlock, type "ROW-COLUMN", ex: 1-3.')

    while unsolved:
        print(f'{puzzle[0]}\n{puzzle[1]}')
        user_input = input(f'ROW-COLUMN: ')
        split_input = user_input.lower().split(sep='-')
        try:
            row = split_input[0]
            column = split_input[1]
        except IndexError:
            print('This is not a valid input.')
            continue

        if digit_match(row) and digit_match(column):
            try:
                puzzle[int(row)-1][int(column)-1] = [False]
            except:
                print('This row and column does not work.')
        unsolved = check_puzzle(puzzle)
    
    return True


def check_puzzle(puzzle) -> bool:
    for row in puzzle:
            for column in row:
                if not column[0]:
                    continue
                else:
                    return True
    return False

def unlock_room(location: type[Location]):
    if location.is_locked:
        solve()
        location.unlock_room()
        print("Unlocked.")
    else:
        print('This location is not locked.')
    return None


if __name__ == '__main__':
    solve(make_puzzle())
# sqlite_main.py
# main handler for dice poker game.
# fields interaction between the user and dice handler objects
# author: pcostjr
# created: 1.23.2025
# last update: 1.15.2026

# import local modules
from dice import Dice
from display import display_dice
import random
import time
# configuration to use inquirer package
import os
import sys
sys.path.append(os.path.realpath("."))
import inquirer

title = (f"[-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-]\n"
         f"██████╗██╗█████████████╗    ██████╗ ██████╗██╗  ███████████████╗\n"
         f"██╔══██████╔════██╔════╝    ██╔══████╔═══████║ ██╔██╔════██╔══██╗\n"
         f"██║  ██████║    █████╗      ██████╔██║   ███████╔╝█████╗ ██████╔╝\n"
         f"██║  ██████║    ██╔══╝      ██╔═══╝██║   ████╔═██╗██╔══╝ ██╔══██╗\n"
         f"██████╔██╚█████████████╗    ██║    ╚██████╔██║  ███████████║  ██║\n"
         f"╚═════╝╚═╝╚═════╚══════╝    ╚═╝     ╚═════╝╚═╝  ╚═╚══════╚═╝  ╚═╝\n"
         f"[-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-][-]\n")

# used for clearing the terminal
# os.system('cls' if os.name == 'nt' else 'clear')


def prompt_message(in_message, in_choices):
    # prompt question from input
    question = [
        inquirer.List(
            "choice",
            message=in_message,
            choices=in_choices,
        ),
    ]

    # parse and return the response
    answer = inquirer.prompt(question)
    # clears the terminal on both windows and linux
    os.system('cls' if os.name == 'nt' else 'clear')
    return answer["choice"]


# text-based animation that flicks through a bunch of random dice rolls
def rolling_dice_anim(dice):
    fake_rolls = 10
    dice_sides = 6
    delay = 0.1
    fake_dice = []
    for roll in range(fake_rolls):
        fake_dice.clear()
        # quickly generate a random list of integers
        for i in range(len(dice)):
            if dice.is_unlocked(i):
                fake_dice.append(random.randint(1, dice_sides))
            else:
                fake_dice.append(dice.get_value_at(i))
        os.system('cls' if os.name == 'nt' else 'clear')
        print(display_dice(fake_dice))
        time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print(title)
    choice = prompt_message("", ["Start Game", "Quit"])
    if choice == "Quit":
        exit()
    else:
        running = True
        while running:
            # create a new DicePoker Object to run the game
            dp = Dice()
            max_turn = 2

            for turn in range(max_turn + 1):
                # roll dice
                dp.roll_dice()
                rolling_dice_anim(dp)

                # while user is still selecting
                in_turn = True
                lockout_list = []
                while dp.dice_available() and in_turn:
                    print(dp)
                    print(f"Turn {turn + 1} ({max_turn - turn} remaining):\n")
                    choice = prompt_message("Choose which die you'd like to keep", ["Re-roll", 1, 2, 3, 4, 5])

                    # skip turn or keep selection
                    if choice == "Re-roll":
                        in_turn = False
                    else:
                        # if we don't already have the lockout queued, and that die is unlocked
                        if choice not in lockout_list and dp.is_unlocked(choice - 1):
                            lockout_list.append(choice)
                        # toggle the die's keep state. this can be done any amount of times on the same turn
                        dp.toggle_die(choice)

                # locks the dice that were kept after this turn, so they can't be un-kept afterward
                for i in lockout_list:
                    dp.lock_die(i)

            print(dp.score())

            choice = prompt_message("Would you like to play again?", ["Yes", "No"])
            if choice == "No":
                print("Thanks for playing my game!")
                exit()







if __name__ == "__main__":
    main()

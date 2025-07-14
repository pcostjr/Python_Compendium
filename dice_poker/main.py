# sqlite_main.py
# main handler for dice poker game.
# fields interaction between the user and dicepoker
# author: signal
# created: 1.23.2025
# last update: 1.26.2025

# configuration to use inquirer package
import os
import sys
sys.path.append(os.path.realpath("."))
import inquirer  # noqa

# import dicepoker object from library
from dicepoker import DicePoker

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
    # os.system('cls' if os.name == 'nt' else 'clear')
    return answer["choice"]



def main():
    print(title)
    choice = prompt_message("", ["Start Game", "Quit"])
    if choice == "Quit":
        exit()
    else:
        running = True
        while running:
            # create a new DicePoker Object to run the game
            dp = DicePoker()
            max_turn = 2

            for turn in range(max_turn + 1):
                # roll dice
                dp.roll_dice()

                # while user is still selecting
                in_turn = True
                lockout_list = []
                while dp.dice_available() and in_turn :
                    # turn output, shows the current state of the dice.
                    print(f"Turn {turn + 1} ({max_turn - turn} remaining):\n")
                    print(dp)
                    choice = prompt_message("Choose which die you'd like to keep", [1,2,3,4,5,
                                                                                    "Re-roll"])

                    # skip turn or keep selection
                    if choice == "Re-roll":
                        in_turn = False
                    else:
                        # if we don't already have the lockout queued, and that die is unlocked
                        if choice not in lockout_list and dp.is_unlocked(choice):
                            lockout_list.append(choice)
                        # toggle the die's keep state. this can be done any amount of times on the same turn
                        dp.toggle_die(choice)

                # locks the dice that were kept after this turn so they can't be un-kept afterward
                for i in lockout_list:
                    dp.lock_die(i)

            print(dp.score())

            choice = prompt_message("Would you like to play again?", ["Yes", "No"])
            if choice == "No":
                print("Thanks for playing my game!")
                exit()












if __name__ == "__main__":
    main()

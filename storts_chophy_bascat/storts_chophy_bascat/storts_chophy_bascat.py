# storts_chophy_bascat.py
# description: A simple terminal-based version of world
# author: pcostjr
# created: 11.03.2025
# last update: 11.03.2025

# import statements
import random
import inquirer3
import sys
import os

# the exact length of words to be used for the game
WORD_LEN = 5
MAX_TRIES = 5
WORD_LIST = []

# Process a request with options using inquirer3
def prompt_list_question(in_message, in_choices):
    # prompt question from input
    question = [
        inquirer3.List(
            "choice",
            message=in_message,
            choices=in_choices,
        ),
    ]
    # parse and return the response
    answer = inquirer3.prompt(question)
    # clears the terminal on both windows and linux
    os.system('cls' if os.name == 'nt' else 'clear')
    return answer["choice"]

def prompt_text_question(in_message):
    question = [
        inquirer3.Text(
            "answer",
                   message=in_message)
    ]
    answer = inquirer3.prompt(question)
    os.system('cls' if os.name == 'nt' else 'clear')
    return answer["answer"]

def populate_wordlist():
    with open("assets/words_alpha.txt", "r") as dictionary:
        for word in dictionary.readlines():
            if len(word.strip()) == WORD_LEN:
                WORD_LIST.append(word.strip())

def play_game():
    tries = MAX_TRIES
    game_string = f"Tries Remaining: {"♥"*tries}"
    print(game_string)
    try:
        while True:
            response = prompt_text_question("Enter a guess: ")
            if len(response.strip()) != WORD_LEN:
                print(f"Error! Please enter a guess of exactly {WORD_LEN} letters.")
            else:
                break
    except:
        print("An error has occurred.")



def main():
    populate_wordlist()
    play_game()

if __name__ == "__main__":
    main()

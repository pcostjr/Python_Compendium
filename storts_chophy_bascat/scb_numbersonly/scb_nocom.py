# scb_nocom.py
# description: A simple number-guessing game similar to Pico Fermi Bagels
# this time with zero comments
# author: pcostjr
# created: 11.03.2025
# last update: 11.03.2025

import random

MIN_VAL = 100
MAX_VAL = 999


def generate_number_list():
    value = random.randint(MIN_VAL, MAX_VAL)
    return str(value)


def main():
    target = generate_number_list()
    print(f"Target is: {target}")

    guess = input("Please enter a three-digit number.")
    response = ["Bascat" for i in range(len(target))]

    if guess == target:
        print("Yay! You solved the puzzle!")
    else:
        for g_digit in range(len(guess)):
            for t_digit in range(len(target)):
                if guess[g_digit] == target[t_digit]:
                    if g_digit == t_digit:
                        response[g_digit] = "Chophy"
                    else:
                        response[g_digit] = "Storts"


    print(response)






if __name__ == '__main__':
    main()

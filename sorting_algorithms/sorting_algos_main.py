# sorting_algos_main.py
# description: main method declaration for the mass sorting algorithm project
# author: pcostjr
# created: 09.18.2024
# last update: 10.29.2025

# TODO: Figure out a prettier way to do this later
from s01_bubble_sort import bubble_sort
from s02_selection_sort import selection_sort
from s03_insertion_sort import insertion_sort
from s04_merge_sort import merge_sort


# import libraries
import random
import inquirer3
import time
import os
import sys
sys.path.append(os.path.realpath("."))

# default configuration for list size and boundaries
LOWER_BOUND = -100
UPPER_BOUND = 100
LIST_LEN = 10000
MAX_DISPLAY = 20
LOGO = """  █████████                   █████   ███                        █████████ ████                           ███ █████  █████                         
 ███░░░░░███                 ░░███   ░░░                        ███░░░░░██░░███                          ░░░ ░░███  ░░███                          
░███    ░░░  ██████ ████████ ███████ ████████████   ███████    ░███    ░███░███  ███████ ██████ ████████ ███████████ ░███████ █████████████  █████ 
░░█████████ ███░░██░░███░░██░░░███░ ░░██░░███░░███ ███░░███    ░███████████░███ ███░░██████░░██░░███░░██░░██░░░███░  ░███░░██░░███░░███░░██████░░  
 ░░░░░░░░██░███ ░███░███ ░░░  ░███   ░███░███ ░███░███ ░███    ░███░░░░░███░███░███ ░██░███ ░███░███ ░░░ ░███ ░███   ░███ ░███░███ ░███ ░██░░█████ 
 ███    ░██░███ ░███░███      ░███ ██░███░███ ░███░███ ░███    ░███    ░███░███░███ ░██░███ ░███░███     ░███ ░███ ██░███ ░███░███ ░███ ░███░░░░███
░░█████████░░██████ █████     ░░█████████████ ████░░███████    █████   ████████░░██████░░██████ █████    █████░░█████████ █████████░███ ██████████ 
 ░░░░░░░░░  ░░░░░░ ░░░░░       ░░░░░░░░░░░░░ ░░░░░ ░░░░░███   ░░░░░   ░░░░░░░░░ ░░░░░███░░░░░░ ░░░░░    ░░░░░  ░░░░░░░░░ ░░░░░░░░░ ░░░ ░░░░░░░░░░  
                                                   ███ ░███                     ███ ░███                                                           
                                                  ░░██████                     ░░██████                                                            
                                                   ░░░░░░                       ░░░░░░                                                             """


# Process a request with options using inquirer3
def prompt_list_message(in_message, in_choices):
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


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_list():
    if LIST_LEN < 2:
        print("Error! List length is too small. Please select a length greater than 1.")
    else:
        # generate a list of random numbers from lower to upper
        number_list = [random.randint(LOWER_BOUND, UPPER_BOUND) for i in range(LIST_LEN)]
    return number_list


# run the specified sort
def do_sort(sort_type, number_list):
    # display unsorted list
    if LIST_LEN > MAX_DISPLAY:
        # truncate list length when displaying if significantly large
        print(f"Initial Values = " + str(number_list[:10]) + " ... " + str(number_list[-10:]))
    else:
        print(f"Initial Values = {number_list}")

    # actually do the sort
    # snapshot time
    start_time = time.time()
    match sort_type:
        case "Bubble Sort":
            number_list, s_actions, s_loops = bubble_sort(number_list)
        case "Selection Sort":
            number_list, s_actions, s_loops = selection_sort(number_list)
        case "Insertion Sort":
            number_list, s_actions, s_loops = insertion_sort(number_list)
        case "Merge Sort":
            number_list, s_actions, s_loops = merge_sort(number_list)
    elapsed_time = time.time() - start_time

    # display sorted list
    if LIST_LEN > MAX_DISPLAY:
        # truncate list length when displaying if significantly large
        print(f"Sorted Values = " + str(number_list[:10]) + " ... " + str(number_list[-10:]))
    else:
        print(f"Sorted Values = {number_list}")

    # display metrics
    print(f"{sort_type} completed in {round(elapsed_time, 3)}s\n"
          f"Total Actions: {'{:,}'.format(s_actions)}\n"
          f"Total Iterations: {'{:,}'.format(s_loops)}")


# main method declaration
def main():
    print(LOGO)
    time.sleep(0.5)
    clear_screen()
    # initial list gen
    number_list = generate_list()
    while True:
        # nts: can't use line breaks on prompt message.
        response = prompt_list_message("Please choose an option:",
                              ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort",
                               "Regenerate List", "View List Contents", "Modify List", "Exit"])
        match response:
            case "Exit":
                print("Goodbye!")
                exit()
            case "Modify List":
                # TODO: Add inquirer input to do modifications
                print("Sorry, I can't do that right now.")
            case "Regenerate List":
                number_list = generate_list()
            case "View List Contents":
                print(number_list)
                print(f"Total Values = {'{:,}'.format(LIST_LEN)}\n"
                      f"Lower Bound = {'{:,}'.format(LOWER_BOUND)}\n"
                      f"Upper Bound = {'{:,}'.format(UPPER_BOUND)}")
            case "Bubble Sort":
                # we 'slice' the entire list to make a copy to bypass pass-by-value-reference
                # otherwise, number_list itself will be sorted on
                do_sort("Bubble Sort", number_list[:])
            case "Selection Sort":
                do_sort("Selection Sort", number_list[:])
            case "Insertion Sort":
                do_sort("Insertion Sort", number_list[:])
            case "Merge Sort":
                do_sort("Merge Sort", number_list[:])

if __name__ == "__main__":
    main()

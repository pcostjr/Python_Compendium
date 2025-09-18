# apples.py
# description: A simple program that demonstrates loops, menu items, and processing data.
# created: 09.17.2025
# last_update: 09.18.2025
# author: pcostjr
import os

def main():
    while True:
        print("[-] 0. Exit\n"
              "[-] 1. Add apples to count\n"
              "[-] 2. Make item(s)")

        selection = int(input("[-] Please select an option: "))

        # clear the terminal. Selects for Windows cls command and Linux clear command.
        os.system('cls' if os.name == 'nt' else 'clear')

        if selection == 0:
            exit()
        elif selection == 1:
            print("Adding apples!")
            input("input to stop program for testing")
        elif selection == 2:
            print("Making items.")
        else:
            print("[!] Error: Please select a valid option.")


if __name__ == "__main__":
    main()

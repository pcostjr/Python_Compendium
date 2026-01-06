# enigma.py
# description: a simple rotational ciphertext program that can create
# custom encoded messages, as well as encode and decode from file.
# author: pcostjr
# created: 11.13.2024
# last update: 5.12.2025
import random

# we'll be using this string for the majority of our translations
alphabet = "abcdefghijklmnopqrstuvwxyz"

# encode a message using a rotational cipher
def encode_message():
    message = input("Please enter the message you'd like to encode: ").lower()
    key = int(input("Enter the rotational cipher key. (Press enter for a random value)") or random.randint(0,26))

    # search for the corresponding character if it is alphabetical.
    # then, shift the letter forward by key, rotating back to the top of the alphabet if we exceed it.
    ciphertext = ""
    for char in message:
        if char.isalpha():
            ciphertext += alphabet[(alphabet.index(char) + key) % 26]
        else:
            ciphertext += char

    print(f"Used key of {key} Encoded message is:\n{ciphertext}")

    # choice to output to existing or new file. Default option just returns to menu
    selection = input("Would you like to write this output to a file? (y/N)")
    if selection == "y":
        filename = input("Enter the filename you'd like to write to.")
        with open(filename, 'w') as file:
            file.write(ciphertext)

# encode a message from a text file
def encode_file():
    # get the filename and rotation for encoding
    filename = input("Please enter the filename of the message you'd like to encode: ")
    key = int(input("Enter the rotational cipher key. (Press enter for a random value) ") or random.randint(0,26))

    # translate any alphabetical characters using the rotational cipher
    # ignore numbers and symbols
    ciphertext = ""
    with open(filename, 'r') as file:
        message = file.read().lower()
    for char in message:
        if char.isalpha():
            ciphertext += alphabet[(alphabet.index(char) + key) % 26]
        else:
            ciphertext += char

    print(f"Used key of {key} Encoded message is:\n{ciphertext}")

    selection = input("Select an option: (Press Enter to return to main menu):\n"
                      "[1]: Overwrite existing file with encoded message.\n"
                      "[2]: Create new file with encoded message.")

    # write to file or to a new file
    if selection == "1":
        with open(filename, 'w') as file:
            file.write(ciphertext)
    elif selection == "2":
        filename = input("Enter the filename you'd like to write to.")
        with open(filename, 'w') as file:
            file.write(ciphertext)

# decode from a file with a given key
def decode_file():
        wait_file = True
        while wait_file:
            ciphertext = ""
            try:
                    filename = input("Please enter the filename of the message you'd like to decode: ")
                    key = int(input("Enter the rotational cipher key. (Press enter if unknown.) ") or -1)

                    if key == -1:
                        # if we do not know the key, guess all possible keys
                        decode_unknown_key(filename)
                    else:
                        with open(filename, 'r') as file:
                            message = file.read().lower()
                        wait_file = False

                    for char in message:
                        if char.isalpha():
                            ciphertext += alphabet[(alphabet.index(char) - key) % 26]
                        else:
                            ciphertext += char

                    print(f"Used key of {key} Decoded message is:\n{ciphertext}")
                    selection = input("Select an option: (Press Enter to return to main menu):\n"
                                      "[1]: Overwrite existing file with decoded message.\n"
                                      "[2]: Create new file with encoded message.")

                    if selection == "1":
                        with open(filename, 'w') as file:
                            file.write(ciphertext)
                    elif selection == "2":
                        filename = input("Enter the filename you'd like to write to.")
                        with open(filename, 'w') as file:
                            file.write(ciphertext)

            except FileNotFoundError as e:
                print("[!] Error: Invalid Filename.")



# runs if the key is unknown. If this is true, print out all possible decoding combinations.
def decode_unknown_key(filename):
    print("Unknown key detected. Printing all possible rotations:")
    for key in range(0, 26):
        ciphertext = ""
        with open(filename, 'r') as file:
            message = file.read().lower()
        for char in message:
            if char.isalpha():
                ciphertext += alphabet[(alphabet.index(char) - key) % 26]
            else:
                ciphertext += char

        print(f"Used key of {key} Decoded message is:\n{ciphertext}")


if __name__ == "__main__":
    while True:
        print(f"Welcome to the Enigma Machine!\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode file.\n"
              f"[3]: Decode file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")
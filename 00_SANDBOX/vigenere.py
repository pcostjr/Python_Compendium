# vigenere.py
# description: A simple, proof of concept program that converts messages using a key with the Vigenere cipher method.
# author: pcostjr
# created: 12.07.2025
# last-update: 12.08.2025

# create dictionary where keys are letters, values are positions
# we could hard code this but I thought I'd get fancy just as a proof of concept
dict_alphabet = {chr(i + ord('A')): i for i in range(26)}

# encode vigenere message using ASCII ordinal values.
def vigenere_ascii(message, key):
    # forces uppercase to standardize the conversion, then converts case later
    encoded = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for letter in message:
        if letter.isalpha():
            # determine case of the letter, force uppercase after
            is_upper = letter.isupper()
            letter = letter.upper()

            # get the ordinal ascii value of the character with respect to the alphabet
            letter_pos = ord(letter) - ord('A')  # 0-25
            # get the ordinal ascii value of the specific shift of the key
            # key_index % key_length creates a repeating pattern for the length of the phrase
            # we index that and get the ordinal value
            key_shift = ord(key[key_index % key_length]) - ord('A')  # 0-25

            # encode the character
            encoded_pos = (letter_pos + key_shift) % 26
            encoded_letter = chr(encoded_pos + ord('A'))

            # preserve the case of the letter
            if not is_upper:
                encoded_letter = encoded_letter.lower()

            # append it to the encoded string
            encoded += encoded_letter
            # increase the index to cycle to the next letter
            key_index += 1
        else:
            # if its not a letter, just append it to the encoded string
            encoded += letter

    return encoded

# encode vigenere using a dictionary
def vigenere_dictionary(message, key):

    encoded = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for letter in message:
        if letter.isalpha():

            is_upper = letter.isupper()
            letter = letter.upper()

            # get positions from dictionary
            char_pos = dict_alphabet[letter]
            key_pos = dict_alphabet[key[key_index % key_length]]

            # Apply Vigenere cipher formula
            encoded_pos = (char_pos + key_pos) % 26

            # Find the letter at the encoded position
            encoded_letter = None
            for new_letter, pos in dict_alphabet.items():
                if pos == encoded_pos:
                    encoded_letter = new_letter
                    break

            if not is_upper:
                encoded_letter = encoded_letter.lower()

            encoded += encoded_letter
            key_index += 1
        else:

            encoded += letter

    return encoded

# main method declaration
def main():
    while True:
        print("Welcome to Vigenere Encoder!\n"
              "[0]. Exit\n"
              "[1]. Encode using ASCII/Ordinal Method\n"
              "[2]. Encode using Dictionary Method\n")
        choice = input("[!]Enter your choice: ").strip()

        if choice == '1':
            print("[-] Ordinal Method")
            message = input("[>] Enter message to encode: ")
            key = input("[>] Enter encryption key: ")

            if not key.isalpha():
                print("[!] Error: Key must contain only letters!")
                continue

            encoded = vigenere_ascii(message, key)
            print(f"[-] Original: {message}\n"
                  f"[-] Key: {key}\n"
                  f"[-] Encoded: {encoded}\n")

        elif choice == '2':
            print("[-] Dictionary Method")
            message = input("[>] Enter message to encode: ")
            key = input("[>] Enter encryption key: ")

            if not key.isalpha():
                print("[!] Error: Key must contain only letters!")
                continue

            encoded = vigenere_dictionary(message, key)
            print(f"[-] Original: {message}\n"
                  f"[-] Key: {key}\n"
                  f"[-] Encoded: {encoded}")

        elif choice == '0':
            print("[-] Exiting")
            exit()

        else:
            print("[!] Error. Invalid Selection.")


if __name__ == "__main__":
    main()
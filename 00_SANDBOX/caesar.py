# caesar.py
# description: A simple program that exemplifies a rotational cipher using different methods
# author: pcostjr
# created: 11.20.2025
# last_update: 11.24.2025

phrase = input("Enter a string:")
ROTATION = 3
UPPER_CASE = 65
LOWER_CASE = 97
ALPHABET_SIZE = 26

# caesar cipher using ordinal values
def cc_ordinal(phrase):
    encrypted = ""
    for letter in phrase:
        # if the letter is a letter
        if letter.isalpha():
            # select the corresponding alphabet value in ascii (A = 65, a = 97)
            charset = (UPPER_CASE if letter.isupper() else LOWER_CASE)
            # cipher the specific letter by getting its ascii value,
            # getting its position in the alphabet
            # increase it ROTATION places 'forward'
            # modulo that value to keep it within 0-25, turn it back into the corresponding letter
            encrypted += chr((ord(letter) - charset + ROTATION) % ALPHABET_SIZE + charset)
        else:
            # if its none of that, just add it to the out string
            encrypted += letter
    # return the newly encrypted string
    return encrypted

def cc_decode(phrase):
    encrypted = ""
    for letter in phrase:
        if letter.isalpha():
            charset = (UPPER_CASE if letter.isupper() else LOWER_CASE)
            # see above for commentary, the only difference is this one subtracts the rotation
            encrypted += chr((ord(letter) - charset - ROTATION) % 26 + charset)
        else:
            encrypted += letter

    return encrypted

UPPER_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
# caesar cipher with two alphabet strings
def cc_string(phrase, rotation):
    # PRECONDITION: The character must be a letter.
    # Determine if the letter is uppercase or lowercase.
    # Find its position in the corresponding alphabet.
    # 'Rotate' that letter's alphabet by rotation spaces. (A = 0 + 3 = index 3)
    # Retrieve the letter at that new location from the list.
    # Add the newly encrypted letter to the cipher string.
    # At the end, return the completed cipher.
    # (((also make the decryption for this too)))
















ciphertext = cc_ordinal(phrase, ROTATION)
print(ciphertext)
print(caesar_cipher_decode(ciphertext, ROTATION))
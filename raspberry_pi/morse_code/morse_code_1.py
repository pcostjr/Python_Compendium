# Tony Le, Andrea Francisco, Nico Bougioukas 3.22.23

import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
buzzer = GPIO.PWM(17, 1000) # 1000 Hz


def get_morse(character) -> list[str]: # Return a list containing a character translated to morse code
    morse_dict = { # Dictionary containing A-Z, 1-9, '. , ? /'
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '-.',
    'H': '...',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '--.--',
    'P': '---',
    'Q': '---.',
    'R': '.--.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--.--',
    '?': '..--..',
    '/': '-..-.',
    ' ': ''
    }
    return [morse_dict[character]]

def buzzer_fn(morse_list) -> None: # Takes the entire list of morse code characters as parameters
    for char in morse_list: # Each individual letter/number/character
        for morse in char: # Each dot, dash, or space
            if morse == '':
                sleep(0.7) # If a space between words, wait 700 ms
            elif morse == '-': 
                buzzer.start(1)
                sleep(0.3)
                buzzer.stop(1)
                sleep(0.3)
            elif morse == '.':
                buzzer.start(0.1)
                sleep(0.1)
                buzzer.stop(0.1)
                sleep(0.1)
        sleep(0.3) # Pause between characters/letters
    return


def main() -> None:
    final: list[str] = []
    original_text: str = input("""
    Input to be translated to morse code:\n
    """)

    characters: list[str] = [*original_text.upper()] # Converts input to individual uppercase characters
    for character in characters:
        temp = get_morse(character) # Get morse code translation of character
        final += temp
    print(final)
    buzzer_fn(final)
    return


if __name__ == '__main__':
    main()
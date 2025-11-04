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
    digits = [int(digit) for digit in str(value)]
    return digits

def main():


if __name__ == '__main__':
    main()

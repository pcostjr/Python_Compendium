# reading_words.py
# description: a simple project demonstrating File IO with the txt file 'words_alpha'.txt
# author: pcostjr
# created 11.03.2025
# last update: 11.03.2025


WORD_LIST = []
WORD_LEN = 5

def extract_words():
    try:
        with open("assets/words_alpha.txt", "r") as file:
            for word in file:
                WORD_LIST.append(word.strip())
    except FileNotFoundError:
        print("[!] Error! File not Found.")


def main():
    extract_words()



if __name__ == "__main__":
    main()
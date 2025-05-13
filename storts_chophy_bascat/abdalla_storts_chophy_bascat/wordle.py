import random
solving = True


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))


def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))


def check(guess, target):
    global solving
    if guess == target:
        print("You guessed the number!")
        solving = False
        play_again = str(input("Do you want to play again? (y/n)").lower())
        if play_again == "y":
            main()
        if play_again == "n":
            exit()
    if solving is True:
        for i in range(len(target)):
            if guess[i] == target[i]:
                prGreen(guess[i])
            else:
                if guess[i] in target:
                    prYellow(guess[i])
                else:
                    prRed(guess[i])


def main():
    life = 0
    digits = 0
    running = True
    print("Welcome to Storts, Chophy, Bascat!")
    prGreen("Chophy is green, and is a right number in the right place")
    prYellow("Storts is yellow, and is a right number in the wrong place")
    prRed("Bascat is red, and is a wrong number.")
    while running is True:
        difficulty = str(input("Choose your difficulty:\n"
                               "Easy: 10 lives with a 3 digit number\n"
                               "Medium: 8 lives with a 4 digit number\n"
                               "Hard: 5 lives with a 5 digit number\n"
                               "Impossible: 3 lives with a 5 digit number. \n"
                               "Choice: ")).lower().strip()
        if difficulty == "easy":
            life = 10
            digits = 3
            running = False
            prGreen(f"You have selected {difficulty}")
        if difficulty == "medium":
            life = 8
            digits = 4
            running = False
            prGreen(f"You have selected {difficulty}")
        if difficulty == "hard":
            life = 5
            digits = 5
            running = False
            prGreen(f"You have selected {difficulty}")
        if difficulty == "impossible":
            life = 3
            digits = 5
            running = False
            prGreen(f"You have selected {difficulty}")
        if running is True:
            prRed("Please choose a provided difficulty")
    t = str(random.randint(10 ** (digits - 1), 9 * (10 ** (digits - 1))))
    game(t, life, digits)


def game(target, lives, digit):
    print(f"Guess a {digit} digit number.")
    run = True
    while run is True and lives != 0:
        prRed(f"Lives Remaining: {'<3 ' * lives}")
        imp = str(input("Guess:"))
        try:
            int(imp)
        except ValueError:
            prRed('Please use numeric digits.')
            prRed(f"'{imp}' is not a valid input")
            continue
        if len(imp) == digit:
            check(imp, target)
        else:
            prRed('Please input the right amount of digits.')
            lives += 1
            # to make sure the lives don't decrease
        global solving
        if solving is not True:
            run = False
        else:
            lives += -1
    if lives == 0:
        prRed(f"You lost! The correct number was {target}")

main()

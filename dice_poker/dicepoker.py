# dicepoker.py
# operates as a handler for several dice, and scoring for a game of dice poker.
# parallel list version.
# author: signal
# created: 1.23.2025
# last update: 1.27.2025

# Scoring Guide
# -------------
# 1. Five of a Kind
# 2. Four of a Kind
# 3. Full House
# 4. Straight ( five consecutive 1's in a row )
# 5. Three of a Kind
# 6. Two Pair
# 1. One pair
# 0. High Die ( Pretty hard to get this one, but possible if you gamble or don't try )

from die import Die

class DicePoker:

    def __init__(self):
        self.MAX_DICE = 5
        self.dice = []
        self.keep = []
        self.lock = []
        self.dice_faces = [0,0,0,0,0,0]


        # for every die allowed in MAX_DICE, generate a die and a corresponding "keep" value.
        for i in range(self.MAX_DICE):
            self.dice.append(Die())
            self.keep.append(True)
            self.lock.append(True)

    # rolls the dice according to whether or not we've kept it.
    def roll_dice(self):
        for i in range(len(self.dice)):
            if self.keep[i]:
              self.dice[i].roll()

    # returns whether we can still have unkept dice
    def dice_available(self):
        count = 0
        for i in range(len(self.keep)):
            if not self.keep[i]:
                count+= 1
        return False if count == 5 else True

    # toggles the keep value of the target die to false so it can't be rerolled, or vice versa
    # note: for index we assume the value entered is the die choice, so we
    # have to decrement it to get the correct index.

    def toggle_die(self, index):
        index -= 1
        # if index is within range, and the die is not turn-locked
        if 0 <= index < len(self.dice) and self.lock[index]:
            self.keep[index] = not self.keep[index]

    # locks the die so it can't be "un-kept" after the turn it was kept on
    def lock_die(self, index):
        index -= 1
        if 0 <= index < len(self.dice):
            self.lock[index] = False

    # returns whether the dice is locked out
    def is_unlocked(self,index):
        index -= 1
        return self.lock[index]

    # determines scoring of dice in priority order
    def score(self):
        result = ""

        for die in self.dice:
            self.dice_faces[die.get_value() - 1] += 1

        print(self.dice_faces)

        if self.of_a_kind(5):
            print("Five of a Kind!")
        elif self.of_a_kind(4):
            print("Four of a Kind!")
        elif self.of_a_kind(3) and self.of_a_kind(2):
            print("Full House!")
        elif self.straight(0, 5) or self.straight(1, 6):
            print("Straight!")
        elif self.of_a_kind(3):
            print("Three of a Kind!")
        elif self.two_pair(2):
            print("Two Pair!")
        elif self.of_a_kind(2):
            print("One Pair!")
        else:
            print("Oof, high die only. How'd you manage that?")

        return result

    # returns if there exists a certain amount "of a kind" in the result list
    # i.e. five of a kind == there is a 5 in the scoring list
    def of_a_kind(self, match):
        if match in self.dice_faces:
            return True
        return False

    # returns if there is a contiguous stream of 1's from start to end
    # constraint: end - start == 5 for this dice game
    def straight(self, start, end):
        result = True
        i = start
        while result and i < end:
            if self.dice_faces != 1:
                result = False
            i += 1
        return result

    # returns whether a pair of values shows up twice in the output
    def two_pair(self, value):
        return self.dice_faces.count(value) == 2


    # readout of current dice and keep status
    def __str__(self):
        out_string = "-------------\n"
        for i in range(len(self.dice)):
            out_string = out_string + f"Die #{i + 1}: {self.dice[i].get_value()}"
            out_string += "\n" if self.keep[i] else "| Kept\n"

        out_string = out_string + "-------------\n"
        return out_string


if __name__ == "__main__":
    dp = DicePoker()
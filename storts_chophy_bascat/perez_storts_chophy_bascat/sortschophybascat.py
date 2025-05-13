# Guessing game that starts out by asking if they are willing to play the game. It can quickly exit out if they don't
# want to play in the first place.


#Imports the random number generator. Furthermore, it also sets session as True, this session is used later on.
import random
session = True


#Function that checks for each index of the guessing number and each number of the user. It returns true if there is a
# number from the user input that matches the guessing number. It returns false if there isn't a number in any position
# that matches one from the guessing number.
def indexnumbersorter(c_number, c_guess, a):
   for i in range(len(c_number)):
       if c_guess[a] == c_number[i]:
           return True
       else:
           return False


# Function that holds the entire program. I have it because I can easily call it back for the continue game function
# I have.
def guessingnumbergame():
# Random number
   guessingnumber = str(random.randint(100, 999))
   lives = 10


# While loop that runs as long as the user has more than zero lives.
   while lives > 0:


#Start of the Try block that checks if the input is a number. If the input is a number it returns True and continues
# running. If it's False, it returns a statement that asks the user to type a valid input.
       v = True
       while v == True:
           try:
               usernumber = (str(input("Choose a number between 100 to 999 !\n")))
               int(usernumber)
               v = False
           except ValueError:
               print("PLEASE USER I NEED A VALID NUMBER INPUT")
# End of try block.
#----------------


# For loop that runs for each index of the user number and returns different inputs depending on if it matches the
# guessing number or if it doesn't.
       for i in range(len(guessingnumber)):


# It returns True for for the function for Storts which means the number exists in the guessing number but it isn't on
# the right place.
           if guessingnumber[i] != usernumber[i] and indexnumbersorter(guessingnumber, usernumber, i) is True:
               print("S")


# It returns False for the function for Bascat which means the number doesn't exist in the guessing number.
           if guessingnumber[i] != usernumber[i] and indexnumbersorter(guessingnumber, usernumber, i) is False:
               print("B")


# Print out C if the number of the user input matches the number AND index of the guessing number.
           if guessingnumber[i] == usernumber[i]:
               print("C")
# Lives system that subtracts one attempt for each attempt.
       print(f"You have {lives - 1} attempts left")
       lives = lives - 1


# Game function that runs at the beginning and at the end of attempts that asks the user if they want to continue
# playing.
while session is True:
   validation = input(f"Would you like to play the game? Type yes or no\n").lower()
   if validation == "yes":
       guessingnumbergame()
   elif validation == "no":
       print("Done playing!")
       session = False











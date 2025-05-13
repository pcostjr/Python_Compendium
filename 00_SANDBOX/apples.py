# apples.py
# description: a simple program explaining basic data storage and control structures for Python
# author: pcostjr
# created: 9.9.2024
# last update: 9.12.2024

apple = float(input("How many apples do you have?"))

response = int(input("Recipe List \n"
                     "============\n"
                     "1. Apple Pie: 7 Apples each\n"
                     "2. Apple Jam: 2.25 Apples each\n"
                     "3. Apple Cider: .5 Apples each\n"
                     "Which item would you like to use your apples on? (1. 2. 3.)\n"))

if response == 1:
    result = int(apple / 7)
    apple = apple % 7
    word = "apple pie"
elif response == 2:
    result = int(apple / 2.25)
    apple = apple % 2.25
    word = "apple jam"
elif response == 3:
    result = int(apple / .5)
    apple = apple % .5
    word = "apple cider"
else:
    print("Error: Invalid Selection. Exiting...")
    exit()

print(f"You've made {result} units of {word} and have {apple} apples left over.")

# FIRST VERSION
# apple = float(input("How many apples do you have?"))
#
#
# pie = int(apple / 7)
# apple = apple % 7
# rpie = apple
#
# jam = int(apple / 2.25)
# apple = apple % 2.25
# rjam = apple
#
# cider = int(apple / .5)
# rcider = apple
#
#
# print(f" You can make {pie} apple pies and have {rpie} apples left over. \n"
#       f" You can make {jam} jars of apple jam and have {rjam} left over. \n"
#       f" You can make {cider} cups of apple cider and have {rcider}left over." )

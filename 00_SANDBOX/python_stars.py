# python_stars.py
# description: a simple program that prints out asterisk 'stars' in specific patterns.
# author: pcostjr
# created: 9.15.2025
# last update: 9.15.2025

for i in range(5):
    print("*")

for i in range(5):
    print("*", end="")
print()
for row in range(6):
    for col in range(0, row + 1):
        print("*", end="")
    print()
print()
for row in range(5,0,-1):
    for col in range(0,row):
        print("*", end="")
    print()
print()
for i in range(5):
    print("*", end="")
print()
for i in range(3):
    print("*",end="")
    for j in range(3):
        print(" ", end="")
    print("*")
for i in range(5):
    print("*", end="")

for row in range(5 + 1):
    for space in range(5 - row):
        print(" ", end="")
    for star in range(2 * row - 1 ):
        print("*", end="")
    print()


# list_examples.py
# description: a simple example of list operations in Python
# author: pcostjr
# date_created: 9.25.2025
# last_update: 9.25.2025


colors = ["red","blue","yellow","orange", "banana", "bornana"]

# print(colors)
# colors.append("periwinkle")
# print(colors)
# colors.insert(0, "chartreuse")
# print(colors)
# colors.insert(5, "magenta")
# print(colors)
# color = colors.pop()
# print(color)
# print(colors)
# colors.remove("blue")
# print(colors)
# colors.remove(colors[len(colors) - 1])

for color in colors:
    print(f"My favorite color is: {color}")

for i in range(len(colors)):
    print(f"My favorite color is: {colors[i]}")


# stack.py
# description: A simple last-in, first-out abstract data type that utilizes a list to store items
# author: pcostjr
# created: 7.9.2025
# last update: 7.9.2025

class Stack:

    # create a new stack instance
    def __init__(self):
        self.items = []

    # returns whether the list is empty
    def is_empty(self):
        return self.items == []

    # append a new item onto the end of the stack
    def push(self, item):
        self.items.append(item)

    # remove an item from the end of the list, and return it
    def pop(self):
        return self.items.pop()

    # return an item from the end of the list without removing it from the stack
    def peek(self):
        return self.items[len(self.items) - 1]

    # return the current size of the stack
    def size(self):
        return len(self.items)

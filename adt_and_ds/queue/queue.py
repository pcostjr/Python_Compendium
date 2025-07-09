# queue.py
# description: A simple first-in, first-out abstract data type
# author: pcostjr
# created: 7.9.2025
# last update: 7.9.2025

class Queue:

    # create a new instance of Queue
    def __init__(self):
        self.items = []

    # returns whether the list is empty
    def is_empty(self):
        return self.items == []

    # prepends and item to the beginning of the list
    def enqueue(self, item):
        self.items.insert(0,item)

    # removes an item from the end of the list, and returns it
    def dequeue(self):
        return self.items.pop()

    # return the current size of the queue
    def size(self):
        return len(self.items)
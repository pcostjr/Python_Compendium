# doublelist.py
# description: doubly linked list built to specification in the Assignment 4 outline
# author: pcostjr
# created: 4.18.2024
# last update: 4.18.2024

# I kept Node within the class since it's a bit unnecessary to dedicate an entire .py file to it
class Node:
    # constructor with data passed in, assigns value to pointer
    # we will use this for our links
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

class DoubleList:
    # DLL = Doubly Linked List

    # default constructor. Host the first pointer for the DLL
    def __init__(self):
        # Pythons constructor assigns instance variables already,
        # we do not need separate definitions
        self.first = None

    # returns whether there is an occupied pointer in the list
    def is_empty(self):
        # check to see if the DLL first item is an instance of None
        return self.first is None

    # returns the current size of the DLL
    def size(self):
        size = 0
        current_node = self.first
        # as long as there are items to traverse, keep counting them
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size


    # append a new node to the end of the list
    # I am assuming we are not using a circular list, the lecture touches on it but the interface
    # does not explicitly demand it.
    def append(self, value):
        new_node = Node(value)
        # if we have an empty list, make this item the first
        if self.first is None:
            self.first = new_node
        else:
            # find the last opening
            current_node = self.first
            while current_node.next is not None:
                current_node = current_node.next
            # in order to append, we attach the new node as the next
            current_node.next = new_node
            # and the current_node as previous in our new node.
            new_node.prev = current_node


    # insert into a node, with several cases depending on where we insert the new node
    def insert(self, index, value):
        # if we're out of range, throw an error
        if self.size() < index or index < 0:
            raise IndexError("[!] Error. List index out of range.")
        # if we're just appending to the end of the list with insertion, use the append function we already made
        elif self.size == index:
            self.append(value)
        # otherwise, enter this if/else chain
        else:
            # generate a new Node, and mark our current node
            new_node = Node(value)
            current_node = self.first
            # if we're prepending, append to the beginning by overwriting first, and adding a new next and last
            if index == 0:
                self.first = new_node
                new_node.next = current_node
                current_node.prev = new_node
            # else, find where we are inserting, and reassign the pointers to now add our node to the chain
            else:
                # traverse the DLL
                for i in range(index-1):
                    current_node = current_node.next
                # attach the "left side" chain
                next_node = current_node.next
                current_node.next = new_node
                new_node.prev = current_node
                # attach the "right side" chain
                # if there is a non-None value in the chain, add it to our next
                if next_node is not None:
                    new_node.next = next_node
                    next_node.prev = new_node



    # remove target node in the DLL
    def remove(self, index):
        # if we are out of range, throw an error
        if self.size() < index or index < 0:
            raise IndexError("[!] Error: List index out of range.")
        else:
            # else, traverse the list for the target index
            current_node = self.first
            # if we're removing the first item, reassign the pointers for first
            if index == 0:
                self.first = self.first.next
                # we must also erase the previous link in the chain so it can be garbage collected
                self.first.prev = None
            else:
                # else, locate the target, and reassign the pointers
                for i in range(index-1):
                    current_node = current_node.next
                if current_node is not None:
                    current_node.next = current_node.next.next
                    # we shrink the list by re-assigning the previous link
                    if current_node.next is not None:
                        current_node.next.prev = current_node
                else:
                    current_node.next = None

    # erase the list by dropping the first link in the chain
    # Non-references Nodes are garbage collected
    def clear(self):
        self.first = None

    # return the value stored at the node in a specific index
    def __getitem__(self, index):
        # if we are out of range, throw an error
        if self.size() < index or index < 0:
            raise IndexError("[!] Error: List index out of range.")
        else:
            # else, find the target node, and return its data
            current_node = self.first
            for i in range(index):
                current_node = current_node.next
            return current_node.data

    # represent the DLL in a string format
    def __str__(self):
        return_string = "DLL Contents: ["
        current_node = self.first
        # build onto the string with concatenations
        while current_node is not None:
            return_string += current_node.data.__str__()
            if current_node.next is not None:
                return_string += ", "
            current_node = current_node.next
        return_string += "]"
        return return_string

    def __repr__(self):
        return_string = "DLL Contents: ["
        current_node = self.first
        # build onto the string with concatenations
        while current_node is not None:
            return_string += current_node.data.__str__()
            if current_node.next is not None:
                return_string += ", "
        return_string += "]"
        return return_string
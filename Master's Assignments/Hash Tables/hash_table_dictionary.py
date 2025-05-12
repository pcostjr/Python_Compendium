# hash_table_dictionary.py
# description: A dictionary that inserts, finds, and deletes key value pairs using
# a hash function.
# author: pcostjr
# created: 5.11.2025
# last update: 5.11.2025
import ctypes


# basic data structure for holding key value pairs
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SinglyLinkedList:
    # CONSTRUCTOR
    # initialize an empty hash dictionary
    def __init__(self):
        self.first = None

    # insert value into the beginning of the dictionary list
    # cuts down on recursive calls because we front load the chain
    # instead of appending
    def insert(self, key, value):
        node = Node(key, value)
        if self.first is None:
            self.first = node
        else:
            node.next = self.first
            self.first = node

    # delete target from the chain
    def delete(self, key):
        if self.first is not None:
            if self.first.key == key:
                if self.first.next is not None:
                    # if the first key's chain is not empty, back load
                    # the chain
                    self.first = self.first.next
                else:
                    # else, reset the chain
                    self.first = None
            else:
                node = self.first
                # if not, iterate through the chain until we find the link
                # then erase it by rewriting the links to the surrounding nodes
                while node.next is not None:
                    if node.next.key == key:
                        if node.next.next is not None:
                            node.next = node.next.next
                        else:
                            node.next = None
                    node = node.next

    def clear(self):
        self.first = None

    # primary get function
    # value = collection[key]
    def __getitem__(self, key):
        node = self.first
        # traverse the list, and if we find the key
        # return it, or keep searching
        while node is not None:
            if node.key == key:
                return node.value
            else:
                node = node.next
        # if we traverse the entire dictionary, we don't have the key
        return None

class HashTableDictionary:
    # CONSTRUCTOR
    def __init__(self, m=701):
        self.m = m
        pyarraytype = ctypes.py_object * m
        self.table = pyarraytype()
        for i in range(m):
            # at each index of the table, implement a singly linked list
            # we will use these to append values and append collisions
            # without losing data
            self.table[i] = SinglyLinkedList()

    def key_to_hash(self, key):
        return hash(key)%self.m

    def insert(self, key, value):
        # get the list we're adding to the hash table
        index = self.key_to_hash(key)
        # prepend the value to the corresponding list
        self.table[index].insert(key, value)

    def delete(self, key):
        index = self.key_to_hash(key)
        self.table[key].delete(key)

    def __getitem__(self, key):
        index = self.key_to_hash(key)
        return self.table[key].__getitem__(key)




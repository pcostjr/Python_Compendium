# tree.py
# description: A Python abstract data structure that utilizes nodes connected to one another via
# "left and right" branches. values are stored with associated keys, used to obtain the information.
# author: pcostjr
# created: 5.7.2025
# last update: 5.7.2025


class Node:
    def __init__(self, key, value):
        self.key =  key
        self.data = value
        self.left = None
        self.right = None

    # generate iterator for object node
    def __iter__(self):
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right



class SimpleDict:
    def __init__(self):
        self.root = None

    def get_depth(self, node):
        if node is None:
            return 0
        if node.left is None:
            if node.right is None:
                return 1
            else:
                return self.get_depth(node.right) + 1
        elif node.right is None:
            return self.get_depth(node.left) + 1
        else:
            return max(self.get_depth(node.left), self.get_depth(node.right)) + 1


    def depth(self):
        return self.get_depth(self.root)

    def get_size(self, node):
        if node is None:
            return 0
        if node.left is None:
            if node.right is None:
                return 1
            else:
                return self.get_size(node.right) + 1
        elif node.right is None:
            return self.get_size(node.left)+1
        else:
            return self.get_size(node.left) + self.get_size(node.right) + 1

    # get the length of the tree
    def __len__(self):
        return self.get_size(self.root)

    # gets the target key
    def get(self, node, key):
        # if this node does not exist, raise an Error
        if node is None:
            raise KeyError
        # else, if the key we're looking for is less than the target, delegate left
        if key < node.key:
            return self.get(node.left, key)
        # if the key we're looking for is greater than the target, delegate right
        elif node.key < key:
            return self.get(node.right, key)
        # if not, we must be the target key, return value
        else:
            return node.value

    # get override for data structure, calls get with the current root
    # value = simpleDict[key]
    def __getitem__(self, key):
        return self.get(self.root, key)

    # inserts the key value pair into the tree
    def insert(self, node, key, value):
        # if this node does not exist, create the node with a new key and value pair
        if node is None:
            return Node(key, value)
       # delegate left
        if key < node.key:
            node.left = self.insert(node.left, key, value)
        # delegate right
        elif node.key < key:
            node.right = self.insert(node.right, key, value)
        # if not, we must be the target key, return value
        else:
            node.value = value

    # set override for data structure
    # simpleDict[key] = value
    def __setitem__(self, key, value):
        # set this current root element to the recursively inserted item
        self.root = self.insert(self.root, key, value)

    def is_elem_of(self, node, key):
        # if the key is not here
        if node is None:
            return False
        # delegate left
        elif key < node.key:
            return self.is_elem_of(node.left, key)
        # delegate right
        elif node.key < key:
            return self.is_elem_of(node.right, key)
        # if not, we must be the target key, return value
        else:
            return True

    # determine whether a key exists
    def __contains__(self, key):
        return self.is_elem_of(self.root, key)

    def __iter__(self):
        if self.root:
            # try to find the child objects of the structure
            for node in self.root.__iter__():
                yield node.key



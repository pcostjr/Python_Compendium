# binary_search_tree.py
# description: a simple implementation of a manually-balancing binary
# search tree, as shown in lecture 12-2 where the keys are also the values
# author: pcostjr
# created: 5.7.2025
# last update: 5.10.2025

# ADT Data node for BST
class BSTNode:
    def __init__(self, key):
        # initialize data pointers and left/right attachment points
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    # CONSTRUCTOR METHODS

    # implement a new empty BST. the only data point we need to carry
    # is the root. the rest are self-propagating
    def __init__(self):
        self.root = None

    # ACCESSOR METHODS

    # recursive helper method for size
    def rsize(self, node):
        # if we're looking at an empty node, return 0
        if node is None:
            return 0
        # if not, return the sum of the size of the left and right branches
        # plus 1 for the node we are currently at
        return self.rsize(node.left) + self.rsize(node.right) + 1

    # main method for size
    def size(self):
        return self.rsize(self.root)

    # recursive helper method for height
    def rheight(self, node):
        if node is None:
            return 0
        # if not, return the MAXIMUM between the height of the left and right branches
        # plus 1 for the node we are currently at
        return max(self.rheight(node.left), self.rheight(node.right)) + 1

    # main method for height
    def height(self):
        return self.rheight(self.root)

    # recursive helper method for retrieving items
    def get(self, node, key):
        # if the node doesn't exist at all, raise a key error
        if node is None:
            raise KeyError
        # delegate left
        if key < node.key:
            return self.get(node.left, key)
        # delegate right
        elif node.key < key:
            return self.get(node.right, key)
        # if we do not delegate, we must be at the key, so return it
        else:
            return node.key

    # main method for accessing items based on key
    def __getitem__(self, key):
        return self.get(self.root, key)


    # MUTATOR METHODS

    # recursive helper method for fixing a new node to the tree
    def insert(self, node, key):
        # if the node is none here, we generate a new one
        if node is None:
            return BSTNode(key)
        # delegate and insert left
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            # delegate and insert right
            if node.key < key:
                node.right = self.insert(node.right, key)
            # insert here
            else:
                node.key = key
        # hand the node back to the function call
        return node

    # main method for mutating items (the key is the value so we just)
    # insert it into its proper place in the tree
    def __setitem__(self, key):
        # propagate the node in the correct spot
        self.root = self.insert(self.root, key)

    def peek(self, node, rblist):
        # if there's nothing here, do nothing
        if node is None:
            return
        # append the key value to the list
        rblist.append(node.key)
        # propagate the list by calling the left and right nodes
        self.peek(node.left, rblist)
        self.peek(node.right, rblist)

    # convert the list that was passed in to a binary search tree of nodes
    def treeify(self, rblist):
        # if there is nothing in the list, return nothing
        if len(rblist) == 0:
            return None
        # get the length and midpoint of the list
        l = len(rblist)
        # we do floor division here so python doesn't cast m as a double
        m = l // 2
        # store the current median value into a new BST node
        median = rblist[m]
        m_node = BSTNode(median)
        # set the left and right branches to the recursive treeify
        # of the left half
        # and right half of the current list
        m_node.left = self.treeify(rblist[0:m])
        m_node.right = self.treeify(rblist[m+1:l])
        return m_node

    def rebalance(self):
        # so long as there are nodes to rearrange
        if self.root is not None:
            # temporary rebalance list. We need to start empty
            # so we can append to something
            rblist = []
            # add all of the items in the tree to a list using a peek function
            self.peek(self.root, rblist)
            rblist.sort()
            self.root = self.treeify(rblist)
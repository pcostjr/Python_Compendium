# bst_test.py
# description: test file for BinarySearchTree object
# author: pcostjr
# created: 5.10.2025
# last update: 5.10.2025
import random
from warnings import catch_warnings

from binary_search_tree import BinarySearchTree

bst = BinarySearchTree()
print("Tree Created. Appending 100 random numbers from 0-100")
print("Recording three known values at iteration 5, 10, and 75")

known = []
# add 100 random numbers
for i in range(0,100):

    value = random.randint(0, 100)
    if i in [5,10,75]:
        known.append(value)

    # NOTE: There was a toss up in this, since I am still following the "the keys are the values"
    # from the outline. I could either add a dummy value that I don't use in the bst to account for
    # BST[item] = item, or I could just invoke the set method on its own.
    # I chose to do this even though its a little ugly.
    bst.__setitem__(value)

print(f"Items added. Current size: {bst.size()} Current height: {bst.height()}. Known values are {known}")

print(f"Getting known values: ")

for i in known:
    print(bst[i])

bst.rebalance()
print(f"Rebalancing tree. New size: {bst.size()} New height: {bst.height()}")

print("Ending by searching for item that shouldn't exist")
try:
    print(bst[400])
except:
    print("Get returned an error.")

# main.py
# description: main program for Assignment 4. Runs the Deque and DLL classes through a series of tests.
# author: pcostjr
# created: 4.18.25
# last update: 4.19.2025
import random

from doubly_linked_list import  DoubleList
from deque import Deque

#~~~~~~~~~DEQUE TESTING~~~~~~~~~
# create the deque
dq_test = Deque()

# enqueue left
print(f"Initial deque empty result: {dq_test.is_empty()}")
print("Populating with 5 random values to the left")
for i in range(5):
    dq_test.enqueue_left(random.randint(0,100))
print(dq_test)

# enqueue right
print("Populating with 5 random values from the right")
for i in range(5):
    dq_test.enqueue_right(random.randint(0,100))
print(dq_test)

# dequeue left
print("Popping 3 elements from the left")
for i in range(3):
    print(dq_test.dequeue_left())
print(dq_test)

# dequeue right
print("Popping 3 elements from the right")
for i in range(3):
    print(dq_test.dequeue_right())
print(dq_test)

# peeking
print("Peeking at left and right")
print(f"Peek left: {dq_test.peek_left()}")
print(dq_test)
print(f"Peek right: {dq_test.peek_right()}")
print(dq_test)

# clearing
print("Clearing Deque...")
dq_test.dequeue_all()
print(dq_test)

#~~~~~~~~~DLL TESTING~~~~~~~~~
dll_test = DoubleList()
print("Doubly Linked List Tests:")

# show the empty status
print(f"Initial Status on empty: {dll_test.is_empty()}")
print(dll_test)

# test appending
print("Appending 10 random values between 0 and 100")
for i in range(10):
    dll_test.append(random.randint(0,100))
print(dll_test)

# test size function
print(f"DLL Current size: {dll_test.size()}")


# A small list with different positions to test insertions
positions = [0, dll_test.size(), random.randint(0, dll_test.size())]
# attempt to insert a random value at each position
for index in positions:
    temp = random.randint(0, 100)
    print(f"Attempting insertion of value {temp} at position ({index})")
    dll_test.insert(index, temp)
print("Results: ")
print(dll_test)

# We'll use the same list to attempt removals
for index in positions:
    print(f"Attempting removal of Node at position ({index})")
    dll_test.remove(index)
print("Results: ")
print(dll_test)

# retrieve every item in the list
for i in range(dll_test.size()):
    print(f"Result of accessing index {i}: {dll_test[i]}")

print("Clearing...")
dll_test.clear()

print("Result of clear: ")
print(dll_test)

print("End of test.")
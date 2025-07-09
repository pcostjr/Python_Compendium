from deque import Deque
import random
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
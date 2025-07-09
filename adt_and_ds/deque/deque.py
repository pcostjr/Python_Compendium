# deque.py
# description: A double-ended queue utilizing the Python collections library
# author: pcostjr
# created: 4.19.2025
# last update: 4.19.2025
from collections import deque

class Deque:
    # initialize the deque
    def __init__(self):
        self._queue = deque([])

    # determine if the queue is empty
    def is_empty(self):
        return not self._queue

    # left end functions
    def enqueue_left(self, item):
        self._queue.insert(0, item)

    def dequeue_left(self):
        return self._queue.popleft()

    def peek_left(self):
        return self._queue[0]

    # right end functions
    def enqueue_right(self, item):
        self._queue.append(item)

    def dequeue_right(self):
        return self._queue.pop()

    def peek_right(self):
        return self._queue[len(self._queue) - 1]

    # clear function
    def dequeue_all(self):
        self._queue.clear()

    # string and rep functions for testing
    def __repr__(self):
        return self._queue.__repr__()

    def __str__(self):
        return self._queue.__str__()
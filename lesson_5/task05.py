# Lesson 5
import ctypes
# Task 5.1 (enqueue & dequeue)
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self._size = 0

    # Task 5.2 (complexity)
    # Time complexity O(1)
    # Space complexity O(1)
    def enqueue(self, item):
        if not isinstance(item, Node):
            item = Node(item)

        if self.tail is None:
            self.tail = item
            self.head = item
            self._size += 1
            return

        self.tail.prev = item
        item.next = self.tail
        self.tail = item
        self._size += 1

    # Time complexity O(1)
    # Space complexity O(1)
    def dequeue(self):
        if self.head is None:
            return None

        element = self.head

        if self.head.prev is None:
            self.head = None
            self.tail = None
            self._size -= 1
            return element

        self.head.prev.next = None
        self.head = self.head.prev
        element.prev = None
        element.next = None
        self._size -= 1
        return element

    def size(self):
        return self._size



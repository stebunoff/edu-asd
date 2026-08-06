# Lesson 5
import ctypes

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def enqueue(self, item):
        if self.tail is None:
            self.tail = item
            self.head = item
            self.size += 1
            return

        self.tail.prev = item
        item.next = self.tail
        self.tail = item
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None

        element = self.head

        if self.head.prev is None:
            self.head = None
            self.tail = None
            self.size -= 1
            return element

        self.head.prev.next = None
        self.head = self.head.prev
        element.prev = None
        element.next = None
        self.size -= 1
        return element

    # Task 5.3 (round)
    # Time complexity O(n), where n is number of relocations
    # Space complexity O(1)
    def round(self, n):
        if self.head is None:
            return

        while n > 0:
            self.enqueue(self.dequeue())
            n -= 1

    # Task 5.5 (revert)
    # Time complexity O(n)
    # Space complexity O(1)
    def revert(self):
        if self.head is None:
            return

        item = self.head
        while item is not None:
            prev = item.prev
            item.prev = item.next
            item.next = prev
            item = prev

        self.head, self.tail = self.tail, self.head

# Task 5.4 (two stacks)
# Time complexity O(1) amort.
# Space complexity O(1)
class QueueWithStacks:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, item):
        self.input_stack.append(item)

    def dequeue(self):
        input_stack_len = len(self.input_stack)
        output_stack_len = len(self.output_stack)

        if not input_stack_len and not output_stack_len:
            return None

        if output_stack_len:
            return self.output_stack.pop()

        while len(self.input_stack):
            self.output_stack.append(self.input_stack.pop())

        return self.output_stack.pop()

    def size(self):
        return len(self.input_stack) + len(self.output_stack)

# Task 5.6 (curcular)
class CircularQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")

        self.queue = (capacity * ctypes.py_object)()
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    # Time complexity O(1)
    # Space complexity O(1)
    def enqueue(self, value):
        if self.isQueueFull():
            raise ValueError("Queue is full")

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    # Time complexity O(1)
    # Space complexity O(1)
    def dequeue(self):
        if self.size == 0:
            return None

        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head +1) % self.capacity
        self.size -= 1

        return item

    # Time complexity O(1)
    # Space complexity O(1)
    def isQueueFull(self):
        return self.size == self.capacity

    # Time complexity O(1)
    # Space complexity O(1)
    def peek(self):
        if not self.size:
            return None

        return self.queue[self.head]

рефлексия
3.6 Очень ждал эталонного решения, чтобы убедиться, что реаллокацию лучше выполнять, когда массив заполнен.
3.7 Когда думал над решением, не догадался, что можно не делать многомерный массив, а использовать одномерный. Это уже второе открытие на курсе после индексов циклической очереди.

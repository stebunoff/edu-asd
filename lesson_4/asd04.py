# Lesson 4
# Task 4.1 (methods & tests)
class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    # Time complexity O(1)
    # Space complexity O(1)
    def pop(self):
        if not self.size():
            return None
        
        return self.stack.pop()

    # Time complexity O(1)
    # Space complexity O(1)
    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if not self.size():
            return None

        return self.stack[-1]

# Task 4.2 (head)
class HeadStack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    # Task 4.4 (complexity)
    # Time complexity O(n)
    # Space complexity O(1)
    def pop(self):
        if not self.size():
            return None
        
        return self.stack.pop(0)
    # Task 4.3 (loop)
    # If number of elements in head stack is even, loop prints all elements.
    # If number of elements in head stack is odd, loop prints all elements and None at the end.

    # Time complexity O(n)
    # Space complexity O(1)
    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if not self.size():
            return None

        return self.stack[0]



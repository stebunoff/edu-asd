# Lesson 1
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    # Task 1.4 (find_all)
    # Time complexity O(n)
    # Space complexity O(n)
    def find_all(self, val):
        found = []
        node = self.head

        while node is not None:
            if node.value == val:
                found.append(node)
            node = node.next

        return found

    # Task 1.1 (delete with false flag)
    # Time complexity O(n)
    # Space complexity O(1)

    # Task 1.2 (delete with true flag)
    # Time complexity O(n)
    # Space complexity O(1)
    def delete(self, val, all=False):
        prev = None
        curr = self.head

        while curr is not None:
            if curr.value == val:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next

                if curr is self.tail:
                    self.tail = prev

                if not all:
                    return

                curr = curr.next
            else:
                prev = curr
                curr = curr.next

    # Task 1.3 (clean)
    # Time complexity O(1)
    # Space complexity O(1)
    def clean(self):
        self.head = None
        self.tail = None

    # Task 1.5 (len)
    # Time complexity O(n)
    # Space complexity O(1)
    def len(self):
        length = 0
        node = self.head

        while node is not None:
            length += 1
            node = node.next

        return length

    # Task 1.6 (insert)
    # Time complexity O(1)
    # Space complexity O(1)
    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode

            if self.tail is None:
                self.tail = newNode
        else:
            newNode.next = afterNode.next
            afterNode.next = newNode

            if afterNode is self.tail:
                self.tail = newNode



# Lesson 2
class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    # task 2.1 (find)
    # Time complexity O(n)
    # Space complexity O(1)
    def find(self, val):
        item = self.head

        while item is not None:
            if item.value == val:
                return item
            item = item.next

        return None

    # task 2.2 (find_all)
    # Time complexity O(n)
    # Space complexity O(n)
    def find_all(self, val):
        found = []
        item = self.head
        while item is not None:
            if item.value == val:
                found.append(item)
            item = item.next
        
        return found

    # task 2.3 (delete with false flag)
    # Time complexity O(n)
    # Space complexity O(1)

    # task 2.4 (delete with true flag)
    # Time complexity O(n)
    # Space complexity O(1)
    def delete(self, val, all=False):
        item = self.head
        while item is not None:
            if item.value == val:
                if item.prev is None:
                    self.head = item.next
                else:
                    item.prev.next = item.next
                
                if item.next is None:
                    self.tail = item.prev
                else:
                    item.next.prev = item.prev 

                if not all:
                    return
            item = item.next

    # task 2.7 (clean)
    # Time complexity O(1)
    # Space complexity O(1)
    def clean(self):
        self.head = None
        self.tail = None

    # task 2.8 (len)
    # Time complexity O(n)
    # Space complexity O(1)
    def len(self):
        length = 0
        item = self.head
        while item is not None:
            length += 1
            item = item.next
        return length

    # task 2.5 (insert)
    # Time complexity O(1)
    # Space complexity O(1)
    def insert(self, afterNode, newNode):
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode is None:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            newNode.next = afterNode.next
            if afterNode.next is not None:
                afterNode.next.prev = newNode
            else:
                self.tail = newNode
            afterNode.next = newNode
            newNode.prev = afterNode

    # task 2.6 (add_in_head)
    # Time complexity O(1)
    # Space complexity O(1)
    def add_in_head(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode



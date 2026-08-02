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

    # task 2.10 (revert)
    # Time complexity O(n)
    # Space complexity O(1)
    def revert(self):
        if self.head is None:
            return
        
        item = self.head
        newTail = self.head
        newHead = self.tail
        while item is not None:
            copy = item
            item.next = copy.prev
            item.prev = copy.next
            item = copy.next
        self.head, self.tail = newHead, newTail


    # task 2.11 (cycles check)
    # Time complexity O(n)
    # Space complexity O(n)
    def cycle_presence(self):
        visited = set()
        item = self.head

        while item is not None:
            if item in visited:
                return True

            visited.add(item)
            item = item.next

        return False

    # Time complexity O(n)
    # Space complexity O(1)
    def cycle_presence_floyd(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False

    # Task 2.12 (sort)
    # Time complexity O(n^2)
    # Space complexity O(1)
    def sort(self):
        if self.head is None or self.head.next is None:
            return

        end = None
        left = self.head

        while end is not self.head:
            if left.next is end:
                end = left
                left = self.head
                continue

            right = left.next
            
            if left.value <= right.value:
                left = right
                continue

            left.value, right.value = (right.value, left.value)
            left = right

    # Task 2.13 (merge)
    # Time complexity O(n * k), where k = number of lists and n = number of elements in all lists
    # Space complexity O(k)
    def merge(self, lists):
        for lst in lists:
            lst.sort()

        result = LinkedList2()
        current = [lst.head for lst in lists]

        while True:
            min_node = None
            min_index = None

            for i, node in enumerate(current):
                if node is None:
                    continue

                if min_node is None or node.value < min_node.value:
                    min_node = node
                    min_index = i

            if min_node is None:
                break

            result.add_in_tail(Node(min_node.value))
            current[min_index] = min_node.next

        return result



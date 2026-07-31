# Lesson 1
# Task 1.8 (sum)
# Time complexity O(n)
# Space complexity O(n)
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

    def find_all(self, val):
        found = []
        node = self.head

        while node is not None:
            if node.value == val:
                found.append(node)
            node = node.next

        return found

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

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head

        while node is not None:
            length += 1
            node = node.next

        return length

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

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node.value
            node = node.next

def sum_lists(first, second):
    if first.len() == second.len():
        summarized = LinkedList()
        for a, b in zip(first, second):
            summarized.add_in_tail(Node(a + b))
        return summarized

рефлексия
До обратной связи по стилю кодирования не понимал, что вкладывать цикл в if плохо. Нужно было воспользоваться ранним выходом из функции.
Если бы я пошёл путём обхода цикла с ручным сдвигом указателей, то понадобилась бы проверка одного из списков. В моём варианте это делается в zip.



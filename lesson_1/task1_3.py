# Lesson 1
# Task 1.7 (tests)
import unittest

class TestLinkedListLen(unittest.TestCase):

    def test_empty_list_len(self):
        linkedList = LinkedList()
        self.assertEqual(linkedList.len(), 0)

    def test_one_element_list(self):
        linkedList = LinkedList()
        linkedList.add_in_tail(Node(1))
        self.assertEqual(linkedList.len(), 1)

    def test_multiple_elements_list(self):
        linkedList = LinkedList()
        values = list(range(1, 101))

        for value in values:
            linkedList.add_in_tail(Node(value))

        self.assertEqual(linkedList.len(), len(values))

class TestLinkedListInsert(unittest.TestCase):

    def test_empty_list_insert(self):
        linkedList = LinkedList()
        node = Node(10)
        linkedList.insert(None, node)
        self.assertIs(linkedList.head, node)
        self.assertIs(linkedList.tail, node)
        self.assertIsNone(node.next)
        self.assertEqual(linkedList.len(), 1)

    def test_one_element_list_insert(self):
        linkedList = LinkedList()
        linkedList.add_in_tail(Node(1))
        node = Node(2)
        linkedList.insert(linkedList.head, node)
        self.assertEqual(linkedList.len(), 2)
        self.assertIs(linkedList.head.next, node)
        self.assertIs(linkedList.tail, node)
        self.assertIsNone(node.next)

    def test_multiple_elements_list_insert(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        afterNode = linkedList.find(2)
        node = Node(10)
        linkedList.insert(afterNode, node)
        self.assertEqual(linkedList.len(), len(values) + 1)
        self.assertIs(afterNode.next, node)
        self.assertEqual(node.next.value, values[-1])
        self.assertIs(linkedList.tail, node.next)

    def test_multiple_elements_list_insert_at_beginning(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        node = Node(10)
        linkedList.insert(None, node)
        self.assertEqual(linkedList.len(), len(values) + 1)
        self.assertIs(linkedList.head, node)
        self.assertEqual(node.next.value, values[0])
        self.assertEqual(linkedList.tail.value, values[-1])

    def test_multiple_elements_list_insert_at_end(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        afterNode = linkedList.tail
        node = Node(10)
        linkedList.insert(afterNode, node)
        self.assertEqual(linkedList.len(), len(values) + 1)
        self.assertIs(linkedList.tail, node)
        self.assertIs(afterNode.next, node)
        self.assertIsNone(node.next)

    def test_multiple_elements_list_multiple_insert(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        node1 = Node(10)
        node2 = Node(20)
        afterNode = linkedList.find(2)
        linkedList.insert(afterNode, node1)
        linkedList.insert(node1, node2)
        self.assertEqual(linkedList.len(), len(values) + 2)
        self.assertEqual(linkedList.head.value, values[0])
        self.assertEqual(linkedList.head.next.value, values[1])
        self.assertIs(linkedList.head.next.next, node1)
        self.assertIs(node1.next, node2)
        self.assertEqual(node2.next.value, values[-1])
        self.assertIs(linkedList.tail, node2.next)

class TestLinkedListFindAll(unittest.TestCase):
    def test_find_all_single_match(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        found = linkedList.find_all(2)
        self.assertEqual(len(found), 1)
        self.assertIs(found[0], linkedList.find(2))

    def test_find_all_multiple_matches(self):
        linkedList = LinkedList()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(2)
        node4 = Node(3)
        node5 = Node(2)
        linkedList.add_in_tail(node1)
        linkedList.add_in_tail(node2)
        linkedList.add_in_tail(node3)
        linkedList.add_in_tail(node4)
        linkedList.add_in_tail(node5)
        found = linkedList.find_all(2)
        self.assertEqual(len(found), 3)
        self.assertIs(found[0], node2)
        self.assertIs(found[1], node3)
        self.assertIs(found[2], node5)

    def test_find_all_no_matches(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        found = linkedList.find_all(10)
        self.assertEqual(found, [])

    def test_find_all_empty_list(self):
        linkedList = LinkedList()
        found = linkedList.find_all(1)
        self.assertEqual(found, [])

class TestLinkedListClean(unittest.TestCase):

    def test_clean_non_empty_list(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        linkedList.clean()
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)
        self.assertEqual(linkedList.len(), 0)

    def test_clean_empty_list(self):
        linkedList = LinkedList()
        linkedList.clean()
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)
        self.assertEqual(linkedList.len(), 0)

class TestLinkedListDelete(unittest.TestCase):

    def test_delete_from_beginning(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        linkedList.delete(1)
        self.assertEqual(linkedList.len(), 2)
        self.assertEqual(linkedList.head.value, 2)
        self.assertEqual(linkedList.tail.value, 3)

    def test_delete_from_middle(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        linkedList.delete(2)
        self.assertEqual(linkedList.len(), 2)
        self.assertEqual(linkedList.head.value, 1)
        self.assertEqual(linkedList.head.next.value, 3)
        self.assertIs(linkedList.tail, linkedList.head.next)

    def test_delete_from_end(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        linkedList.delete(3)
        self.assertEqual(linkedList.len(), 2)
        self.assertEqual(linkedList.tail.value, 2)
        self.assertIsNone(linkedList.tail.next)

    def test_delete_only_element(self):
        linkedList = LinkedList()
        linkedList.add_in_tail(Node(10))
        linkedList.delete(10)
        self.assertEqual(linkedList.len(), 0)
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)

    def test_delete_only_first_match(self):
        linkedList = LinkedList()
        nodes = [Node(1), Node(2), Node(2), Node(3)]

        for node in nodes:
            linkedList.add_in_tail(node)

        linkedList.delete(2)
        self.assertEqual(linkedList.len(), 3)
        self.assertIs(linkedList.head, nodes[0])
        self.assertIs(linkedList.head.next, nodes[2])
        self.assertIs(linkedList.head.next.next, nodes[3])
        self.assertIs(linkedList.tail, nodes[3])
        self.assertIsNone(linkedList.tail.next)

    def test_delete_all_matches(self):
        linkedList = LinkedList()
        values = [2, 1, 2, 2, 3, 2]

        for value in values:
            linkedList.add_in_tail(Node(value))

        linkedList.delete(2, all=True)
        self.assertEqual(linkedList.len(), 2)
        self.assertEqual(linkedList.head.value, 1)
        self.assertEqual(linkedList.tail.value, 3)
        self.assertIs(linkedList.head.next, linkedList.tail)
        self.assertIsNone(linkedList.tail.next)

    def test_delete_missing_value(self):
        linkedList = LinkedList()
        values = [1, 2, 3]

        for value in values:
            linkedList.add_in_tail(Node(value))

        oldHead = linkedList.head
        oldTail = linkedList.tail
        linkedList.delete(10)
        self.assertEqual(linkedList.len(), 3)
        self.assertIs(linkedList.head, oldHead)
        self.assertIs(linkedList.tail, oldTail)

    def test_delete_from_empty_list(self):
        linkedList = LinkedList()
        linkedList.delete(10)
        self.assertIsNone(linkedList.head)
        self.assertIsNone(linkedList.tail)
        self.assertEqual(linkedList.len(), 0)



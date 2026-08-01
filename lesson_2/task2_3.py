# Lesson 2
import unittest

class TestLinkedList2Find(unittest.TestCase):
    def test_find_empty_list(self):
        linked_list = LinkedList2()
        self.assertEqual(linked_list.find(1), None)

    def test_find_nonempty_list_one_match(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(2)]

        for node in nodes:
            linked_list.add_in_tail(node)

        self.assertIs(linked_list.find(2), nodes[1])

    def test_find_nonempty_list_no_matches(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(2)]

        for node in nodes:
            linked_list.add_in_tail(node)

        self.assertIsNone(linked_list.find(3))

class TestLinkedList2FindAll(unittest.TestCase):
    def test_find_all_empty_list(self):
        linked_list = LinkedList2()
        self.assertEqual(linked_list.find_all(1), [])

    def test_find_all_nonempty_list_one_match(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(2)]

        for node in nodes:
            linked_list.add_in_tail(node)

        self.assertEqual(linked_list.find_all(2), [nodes[1], nodes[2]])

    def test_find_all_nonempty_list_no_matches(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(2)]

        for node in nodes:
            linked_list.add_in_tail(node)

        self.assertEqual(linked_list.find_all(3), [])

class TestLinkedList2Delete(unittest.TestCase):
    def test_delete_from_beginning(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        linked_list.delete(1)
        self.assertEqual(linked_list.len(), 2)
        self.assertIs(linked_list.head, nodes[1])
        self.assertIs(linked_list.tail, nodes[2])
        self.assertIsNone(linked_list.head.prev)
        self.assertIsNone(linked_list.tail.next)
        self.assertIs(linked_list.head.next, linked_list.tail)
        self.assertIs(linked_list.tail.prev, linked_list.head)

    def test_delete_from_middle(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        linked_list.delete(2)
        self.assertEqual(linked_list.len(), 2)
        self.assertIs(linked_list.head, nodes[0])
        self.assertIs(linked_list.tail, nodes[2])
        self.assertIs(linked_list.tail.prev, linked_list.head)
        self.assertIs(linked_list.head.next, linked_list.tail)
        self.assertIsNone(linked_list.head.prev)
        self.assertIsNone(linked_list.tail.next)

    def test_delete_from_end(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        linked_list.delete(3)
        self.assertEqual(linked_list.len(), 2)
        self.assertIs(linked_list.head, nodes[0])
        self.assertIs(linked_list.tail, nodes[1])
        self.assertIs(linked_list.tail.prev, linked_list.head)
        self.assertIs(linked_list.head.next, linked_list.tail)
        self.assertIsNone(linked_list.head.prev)
        self.assertIsNone(linked_list.tail.next)

    def test_delete_with_true_flag(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(2)]

        for node in nodes:
            linked_list.add_in_tail(node)

        linked_list.delete(2, all=True)
        self.assertEqual(linked_list.len(), 1)
        self.assertIs(linked_list.head, nodes[0])
        self.assertIs(linked_list.tail, nodes[0])
        self.assertIsNone(linked_list.head.prev)
        self.assertIsNone(linked_list.tail.next)

class TestLinkedList2Insert(unittest.TestCase):
    def test_insert_in_empty_list(self):
        linked_list = LinkedList2()
        node = Node(1)
        linked_list.insert(None, node)

        self.assertEqual(linked_list.len(), 1)
        self.assertIs(linked_list.head, node)
        self.assertIs(linked_list.tail, node)
        self.assertIsNone(linked_list.head.prev)
        self.assertIsNone(linked_list.tail.next)

    def test_insert_in_tail(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        node = Node(4)
        linked_list.insert(None, node)
        self.assertEqual(linked_list.len(), 4)
        self.assertIs(linked_list.head, nodes[0])
        self.assertIs(linked_list.tail, node)
        self.assertIsNone(linked_list.tail.next)
        self.assertIs(linked_list.tail.prev, nodes[2])
        self.assertIs(nodes[2].next, node)

    def test_insert_after_node(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        node = Node(4)
        linked_list.insert(nodes[1], node)
        self.assertEqual(linked_list.len(), 4)
        self.assertIs(linked_list.head, nodes[0])
        self.assertIs(linked_list.tail, nodes[2])
        self.assertIs(nodes[1].next, node)
        self.assertIs(node.prev, nodes[1])
        self.assertIs(nodes[2].prev, node)
        self.assertIs(node.next, nodes[2])

class TestLinkedList2AddInHead(unittest.TestCase):
    def test_add_in_head_in_empty_list(self):
        linked_list = LinkedList2()
        node = Node(1)
        linked_list.add_in_head(node)
        self.assertEqual(linked_list.len(), 1)
        self.assertIs(linked_list.head, node)
        self.assertIs(linked_list.tail, node)
        self.assertIsNone(node.prev)
        self.assertIsNone(node.next)

    def test_add_in_head_in_nonempty_list(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        node = Node(4)
        linked_list.add_in_head(node)
        self.assertEqual(linked_list.len(), 4)
        self.assertIs(linked_list.head, node)
        self.assertIs(nodes[0].prev, node)
        self.assertIs(node.next, nodes[0])
        self.assertIsNone(node.prev)
        self.assertIs(linked_list.tail, nodes[2])
        self.assertIsNone(linked_list.tail.next)

class TestLinkedList2Clean(unittest.TestCase):
    def test_clean(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        linked_list.clean()
        self.assertEqual(linked_list.len(), 0)
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

class TestLinkedList2Len(unittest.TestCase):
    def test_len_empty_list(self):
        linked_list = LinkedList2()
        self.assertEqual(linked_list.len(), 0)

    def test_len_nonempty_list(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        self.assertEqual(linked_list.len(), 3)

class TestLinkedList2Revert(unittest.TestCase):
    def test_revert_empty_list(self):
        linked_list = LinkedList2()
        linked_list.revert()
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)
        self.assertEqual(linked_list.len(), 0)

    def test_revert_one_element_list(self):
       linked_list = LinkedList2() 
       node = Node(1)
       linked_list.add_in_tail(node)
       linked_list.revert()
       self.assertIs(self.head, node)
       self.assertIs(self.tail, node)
       self.assertEqual(linked_list.len(), 1)
       self.assertIsNone(node.prev)
       self.assertIsNone(node.next)

    def test_revert_list(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        linked_list.revert()
        self.assertIs(linked_list.head, nodes[2])
        self.assertIs(linked_list.tail, nodes[0])
        self.assertIs(nodes[0].prev, nodes[1])
        self.assertIsNone(nodes[0].next)
        self.assertIs(nodes[1].prev, nodes[2])
        self.assertIs(nodes[1].next, nodes[0])
        self.assertIs(nodes[2].next, nodes[1])
        self.assertIsNone(nodes[2].prev)

class TestLinkedList2CyclePresence(unittest.TestCase):
    def test_cycle_presence_empty_list(self):
        linked_list = LinkedList2()
        self.assertEqual(linked_list.cycle_presence(), False)

    def test_cycle_presence_one_element_list(self):
        linked_list = LinkedList2()
        linked_list.add_in_tail(Node(1))
        self.assertEqual(linked_list.cycle_presence(), False)

    def test_cycle_presence_next_item_cycle(self):
        linked_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        linked_list.add_in_tail(node1)
        linked_list.add_in_tail(node2)
        linked_list.add_in_tail(node3)
        node2.next = node1
        self.assertEqual(linked_list.cycle_presence(), True)

    def test_cycle_presence_item_long_cycle(self):
        linked_list = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        linked_list.add_in_tail(node1)
        linked_list.add_in_tail(node2)
        linked_list.add_in_tail(node3)
        node3.next = node1
        self.assertEqual(linked_list.cycle_presence(), True)

    def test_cycle_presence_nonempty_list(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(2), Node(3)]

        for node in nodes:
            linked_list.add_in_tail(node)

        self.assertEqual(linked_list.cycle_presence(), False)

class TestLinkedList2Sort(unittest.TestCase):
    def test_empty_list(self):
        linked_list = LinkedList2()
        linked_list.sort()
        self.assertIsNone(linked_list.head)
        self.assertIsNone(linked_list.tail)

    def test_nonempty_list(self):
        linked_list = LinkedList2()
        nodes = [Node(1), Node(3), Node(2)]

        for node in nodes:
            linked_list.add_in_tail(node)

        linked_list.sort()
        self.assertIs(linked_list.head.value, 1)
        self.assertIs(linked_list.head.next.value, 2)
        self.assertIs(linked_list.tail.value, 3)



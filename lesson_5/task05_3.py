# Lesson 5
import unittest

class TestQueueSize(unittest.TestCase):
    def test_size_empty_list(self):
        queue = Queue()
        self.assertEqual(queue.size(), 0)

    def test_size_nonempty_list(self):
        queue = Queue()
        queue.enqueue(Node(1))
        self.assertEqual(queue.size(), 1)

# Task 5.1 (enqueue & dequeue)
class TestQueueEnqueue(unittest.TestCase):
    def test_enqueue_empty_list(self):
        queue = Queue()
        node = Node(1)
        queue.enqueue(node)
        self.assertEqual(queue.size(), 1)
        self.assertIs(queue.head, node)
        self.assertIs(queue.tail, node)

    def test_enqueue_nonempty_list(self):
        queue = Queue()
        node1 = Node(1)
        node2 = Node(2)
        queue.enqueue(node1)
        queue.enqueue(node2)
        self.assertEqual(queue.size(), 2)
        self.assertIs(queue.head, node1)
        self.assertIs(queue.head.prev, node2)
        self.assertIsNone(queue.head.next)
        self.assertIs(queue.tail, node2)
        self.assertIsNone(queue.tail.prev)
        self.assertIs(queue.tail.next, node1)

# Task 5.1 (enqueue & dequeue)
class TestQueueDequeue(unittest.TestCase):
    def test_dequeue_empty_list(self):
        queue = Queue()
        self.assertIsNone(queue.dequeue())
        self.assertEqual(queue.size(), 0)

    def test_dequeue_one_element_list(self):
        queue = Queue()
        queue.enqueue(Node(1))
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 0)
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_dequeue_nonempty_list(self):
        queue = Queue()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 2)
        self.assertIs(queue.head, node2)
        self.assertIs(queue.head.prev, node3)
        self.assertIsNone(queue.head.next)
        self.assertIs(queue.tail, node3)
        self.assertIsNone(queue.tail.prev)
        self.assertIs(queue.tail.next, node2)

# Task 5.3 (round)
class TestQueueRound(unittest.TestCase):
    def test_round_empty_list(self):
        queue = Queue()
        queue.round(2)
        self.assertEqual(queue.size(), 0)

    def test_round_nonempty_list(self):
        queue = Queue()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        queue.enqueue(node4)
        queue.enqueue(node5)
        queue.round(3)
        self.assertEqual(queue.size(), 5)
        self.assertEqual(queue.head, node4)
        self.assertEqual(queue.tail, node3)
        self.assertIsNone(node4.next)
        self.assertEqual(node4.prev, node5)
        self.assertEqual(node5.next, node4)
        self.assertEqual(node5.prev, node1)
        self.assertEqual(node1.next, node5)
        self.assertEqual(node1.prev, node2)
        self.assertEqual(node2.prev, node3)
        self.assertEqual(node2.next, node1)
        self.assertIsNone(node3.prev)
        self.assertEqual(node3.next, node2)

# Task 5.4 (two stacks)
class TestQueueWithStacksEnqueue(unittest.TestCase):
    def test_qws_nonempty_list(self):
        queue = QueueWithStacks()
        self.assertEqual(queue.dequeue(), None)
        queue.enqueue(1)
        self.assertEqual(queue.size(), 1)
        queue.enqueue(2)
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.size(), 0)

# Task 5.5 (revert)
class TestQueueRevert(unittest.TestCase):
    def test_revert_empty_list(self):
        queue = Queue()
        queue.revert()
        self.assertEqual(queue.size(), 0)

    def test_revert_nonempty_list(self):
        queue = Queue()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        self.assertIs(queue.dequeue(), node1)
        self.assertIs(queue.dequeue(), node2)
        self.assertIs(queue.dequeue(), node3)
        queue.enqueue(node1)
        queue.enqueue(node2)
        queue.enqueue(node3)
        queue.revert()
        self.assertEqual(queue.size(), 3)
        self.assertIs(queue.dequeue(), node3)
        self.assertIs(queue.dequeue(), node2)
        self.assertIs(queue.dequeue(), node1)

# Task 5.6 (curcular)
class TestCircularQueueIsQueueFull(unittest.TestCase):
    def test_empty_list(self):
        queue = CircularQueue(1)
        self.assertFalse(queue.isQueueFull())

    def test_full_queue(self):
        queue = CircularQueue(1)
        queue.enqueue(2)
        self.assertTrue(queue.isQueueFull())

    def test_vacant_space(self):
        queue = CircularQueue(2)
        queue.enqueue(2)
        self.assertFalse(queue.isQueueFull())

    def test_overflow(self):
        queue = CircularQueue(1)
        queue.enqueue(2)
        with self.assertRaises(ValueError):
            queue.enqueue(3)

class TestCircularQueuePeek(unittest.TestCase):
    def test_empty_list(self):
        queue = CircularQueue(1)
        self.assertIsNone(queue.peek())

    def test_one_element_list(self):
        queue = CircularQueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 2)

    def test_multiple_elements_list(self):
        queue = CircularQueue(2)
        queue.enqueue(5)
        queue.enqueue(2)
        self.assertEqual(queue.peek(), 5)

class TestCircularQueue(unittest.TestCase):
    def test_queue(self):
        queue = CircularQueue(2)
        queue.enqueue(2)
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.tail, 1)
        self.assertEqual(queue.head, 0)
        self.assertEqual(queue.peek(), 2)
        queue.enqueue(1)
        self.assertEqual(queue.size, 2)
        self.assertEqual(queue.tail, 0)
        self.assertEqual(queue.head, 0)
        self.assertEqual(queue.peek(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.size, 1)
        self.assertEqual(queue.tail, 0)
        self.assertEqual(queue.head, 1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.size, 0)
        self.assertEqual(queue.tail, 0)
        self.assertEqual(queue.head, 0)
        self.assertIsNone(queue.peek())

    def test_vacant_space_fill(self):
        queue = CircularQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        queue.enqueue(10)
        queue.enqueue(20)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 20)
        self.assertIsNone(queue.dequeue())



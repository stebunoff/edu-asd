# Lesson 3
# Task 3.4 (tests)
class TestDynArrayInsert(unittest.TestCase):

    def test_insert_without_resize(self):
        dyn_array = DynArray()
        dyn_array.insert(0, 1)

        self.assertEqual(dyn_array.count, 1)
        self.assertEqual(dyn_array.capacity, 16)
        self.assertEqual(dyn_array[0], 1)

    def test_insert_with_resize(self):
        dyn_array = DynArray()
        for i in range(0, 18):
            dyn_array.insert(i, i)

        self.assertEqual(dyn_array.count, 18)
        self.assertEqual(dyn_array.capacity, 32)
        self.assertEqual(dyn_array[17], 17)

    def test_insert_index_error(self):
        dyn_array = DynArray()

        with self.assertRaises(IndexError) as cm:
            dyn_array.insert(1, 1)

        self.assertEqual(str(cm.exception), "Index is out of bounds")

class TestDynArrayDelete(unittest.TestCase):

    def test_delete_one_element_without_resize(self):
        dyn_array = DynArray()
        dyn_array.insert(0, 1)
        dyn_array.delete(0)

        self.assertEqual(dyn_array.count, 0)
        self.assertEqual(dyn_array.capacity, 16)

    def test_delete_multiple_elements_without_resize(self):
        dyn_array = DynArray()
        for i in range(0, 8):
            dyn_array.insert(i, i)
        dyn_array.delete(1)
        dyn_array.delete(2)

        self.assertEqual(dyn_array.count, 6)
        self.assertEqual(dyn_array.capacity, 16)
        self.assertEqual(
            [dyn_array[i] for i in range(len(dyn_array))],
            [0, 2, 4, 5, 6, 7]
        )

    def test_delete_element_with_resize(self):
        dyn_array = DynArray()
        for i in range(0, 17):
            dyn_array.insert(i, i)
        dyn_array.delete(1)
        dyn_array.delete(2)

        self.assertEqual(dyn_array.count, 15)
        self.assertEqual(dyn_array.capacity, 21)
        self.assertEqual(
            [dyn_array[i] for i in range(len(dyn_array))],
            [0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        )

    def test_delete_index_error_empty_arr(self):
        dyn_array = DynArray()

        with self.assertRaises(IndexError) as cm:
            dyn_array.delete(0)

        self.assertEqual(str(cm.exception), "Index is out of bounds")

    def test_delete_index_error_nonempty_arr(self):
        dyn_array = DynArray()
        dyn_array.append(1)

        with self.assertRaises(IndexError) as cm:
            dyn_array.delete(100)

        self.assertEqual(str(cm.exception), "Index is out of bounds")

    def test_delete_negative_index_error(self):
        dyn_array = DynArray()
        dyn_array.append(1)

        with self.assertRaises(IndexError) as cm:
            dyn_array.delete(-1)

        self.assertEqual(str(cm.exception), "Index is out of bounds")



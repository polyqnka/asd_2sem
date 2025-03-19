import unittest
from lab2.task3.src.task3 import BST


class TestBST(unittest.TestCase):
    def setUp(self):
        self.tree = BST()
        for key in [10, 5, 15, 2, 7, 12, 20]:
            self.tree.insert(key)

    def test_insert(self):
        self.tree.insert(8)
        self.assertEqual(self.tree.find_min_greater_than(7), 8)

    def test_find_min_greater_than(self):
        self.assertEqual(self.tree.find_min_greater_than(5), 7)
        self.assertEqual(self.tree.find_min_greater_than(10), 12)
        self.assertEqual(self.tree.find_min_greater_than(15), 20)
        self.assertEqual(self.tree.find_min_greater_than(20), 0)


if __name__ == "__main__":
    unittest.main()

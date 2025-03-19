import unittest
from io import StringIO
import sys
from lab2.task1.src.task1 import in_order_traversal, pre_order_traversal, post_order_traversal


class TestBinaryTreeTraversal(unittest.TestCase):
    def setUp(self):
        self.tree = {
            0: (4, 1, 2),
            1: (2, 3, 4),
            2: (6, -1, -1),
            3: (1, -1, -1),
            4: (3, -1, -1)
        }

    def test_in_order_traversal(self):
        result = []
        in_order_traversal(self.tree, 0, result)
        self.assertEqual(result, [1, 2, 3, 4, 6])

    def test_pre_order_traversal(self):
        result = []
        pre_order_traversal(self.tree, 0, result)
        self.assertEqual(result, [4, 2, 1, 3, 6])

    def test_post_order_traversal(self):
        result = []
        post_order_traversal(self.tree, 0, result)
        self.assertEqual(result, [1, 3, 2, 6, 4])


if __name__ == "__main__":
    unittest.main()

import unittest
from tree import Tree

class TestTree(unittest.TestCase):
    def test_find_existing_data(self):
        tree = Tree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        tree.add(5)
        tree.add(6)
        tree.add(7)
        self.assertTrue(tree._find(6, tree.getRoot()))

    def test_find_non_existing_data(self):
        tree = Tree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        tree.add(5)
        tree.add(6)
        tree.add(7)
        self.assertFalse(tree._find(21, tree.getRoot()))

if __name__ == '__main__':
    unittest.main()
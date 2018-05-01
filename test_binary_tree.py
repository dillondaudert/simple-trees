# simple tests
import unittest
import binary_tree as bt
from random import shuffle

class BSTTest(unittest.TestCase):

    def setUp(self):
        values = [1, 0, -2, 18, 10, 11, 6, 9, 20]
        shuffle(values)
        self.values = values
        self.tree = bt.BinarySearchTree()

    def test_root(self):
        self.assertIsNone(self.tree.root)

    def test_insert(self):
        self.tree.insert(5)
        self.assertEqual(self.tree.root.key, 5)

        self.tree.insert(-2)
        self.assertEqual(self.tree.root.lchild.key, -2)

        self.tree.insert(18)
        self.assertEqual(self.tree.root.rchild.key, 18)

    def test_inorder_walk(self):
        self.tree.insert(5)
        self.tree.insert(2)
        self.tree.insert(8)
        self.tree.insert(-10)
        self.tree.insert(100)
        self.tree.insert(-3)
        self.assertEqual(self.tree.inorder_walk(), [-10, -3, 2, 5, 8, 100])

    def test_insert_list(self):
        self.tree.insert(self.values)
        self.assertEqual(self.tree.inorder_walk(), sorted(self.values))

    def test_search(self):
        self.tree.insert(self.values)
        self.assertEqual(self.tree.search(10).key, 10)
        self.assertEqual(self.tree.search(18).key, 18)

        self.assertEqual(self.tree.search(18), self.tree.search(18, kind="recursive"))
        self.assertEqual(self.tree.search(1), self.tree.search(1, kind="recursive"))

        with self.assertRaises(ValueError):
            self.tree.search(18, "magic")
        with self.assertRaises(KeyError):
            self.tree.search(-100)

    def test_delete(self):
        self.tree.insert(self.values)
        values = self.values
        shuffle(values)
        for i in range(len(values)):
            # remove key from beginning
            key = values[0]
            values = values[1:]
            node = self.tree.search(key)
            print(self.tree.inorder_walk())
            self.tree.delete(node)
            # check that we've deleted this node
            self.assertEqual(self.tree.inorder_walk(), sorted(values))



if __name__ == "__main__":
    unittest.main()

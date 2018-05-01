# This implementation comes from the book Introduction to Algorithms, 3rd ed
# by Cormen, Leiserson, Rivest, and Stein.


class BinarySearchTree(object):
    """This tree satisfies the binary search tree property:

    Let x be a node in a binary search tree. If y is a node in the left
    subtree of x, then y.key <= x.key. If y is a node in the right
    subtree of x, then y.key >= x.key.
    """

    _root = None

    def __init__(self, keys: list = []):
        """Initializes a binary search tree, optionally populated with a list
        of keys."""
        if len(keys) > 0:
            self.insert(keys)

    @property
    def root(self):
        return self._root

    def insert(self, key_or_list):
        """Insert key k into the tree. If k is a list of keys, all are
        inserted."""
        if type(key_or_list) == list:
            for key in key_or_list:
                self._insert(key)
        else:
            self._insert(key_or_list)


    def _insert(self, k):
        z = Node(k)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.lchild
            else:
                x = x.rchild
        z._parent = y
        if y is None:
            # tree was empty
            self._root = z
        elif z.key < y.key:
            y._lchild = z
        else:
            y._rchild = z

    def delete(self, z):
        """Delete a node from the tree."""
        if z.lchild is None:
            # replace z with its right child
            self._transplant(z, z.rchild)

        elif z.rchild is None:
            # replace z with its left child
            self._transplant(z, z.lchild)

        else:
            # z has 2 children
            y = self._min(z.rchild)
            if y.parent != z:
                self._transplant(y, y.rchild)
                y._rchild = z.rchild
                y.rchild._parent = y
            self._transplant(z, y)
            y._lchild = z.lchild
            z.lchild._parent = y


    def _transplant(self, u, v):
        """Replace the subtree rooted at u with the subtree rooted at v.
        Node u's parent becomes node v's parent, and node u's parent ends
        up having v as its appropriate child."""

        if u.parent is None:
            self._root = v
        elif u == u.parent.lchild:
            u.parent._lchild = v
        else:
            u.parent._rchild = v
        if v is not None:
            v._parent = u.parent

    def inorder_walk(self):
        return self._inorder_walk(self.root)

    def _inorder_walk(self, x):
        """Return a list of the keys in this tree in sorted order."""
        keys = []
        if x is not None:
            if x.lchild is not None:
                keys.extend(self._inorder_walk(x.lchild))
            keys.append(x.key)
            if x.rchild is not None:
                keys.extend(self._inorder_walk(x.rchild))
        return keys

    def search(self, k, kind:str="iterative"):
        """Search this tree for a key k.
        If the key is not in the tree, returns None."""
        if kind == "iterative":
            x = self._iterative_search(self.root, k)
        elif kind == "recursive":
            x = self._recursive_search(self.root, k)
        else:
            raise ValueError("%s not a valid kind" % kind)

        if x is None:
            raise KeyError("Key %d not found in tree." % k)

        return x


    def _iterative_search(self, x, k):
        while x is not None and k != x.key:
            if k < x.key:
                x = x.lchild
            else:
                x = x.rchild
        return x

    def _recursive_search(self, x, k):
        if k == x.key:
            return x
        if k < x.key and x.lchild is not None:
            return self._recursive_search(x.lchild, k)
        elif k >= x.key and x.rchild is not None:
            return self._recursive_search(x.rchild, k)
        else:
            return None

    def min(self):
        return self._min(self.root)

    def _min(self, x):
        while x.lchild is not None:
            x = x.lchild
        return x

    def max(self):
        return self._max(self.root)

    def _max(self, x):
        while x.rchild is not None:
            x = x.rchild
        return x

    def successor(self, k):
        x = self.search(k)
        return self._successor(x)

    def _successor(self, x):
        """Find the successor of x.key in sorted order."""
        if x.rchild is not None:
            return self._min(x.rchild)

        y = x.parent
        while y is not None and x == y.rchild:
            x = y
            y = y.parent
        return y

    def predecessor(self, k):
        x = self.search(k)
        return self._predecessor(x)

    def _predecessor(self, x):
        """Find the predecessor of x.key in sorted order."""
        if x.lchild is not None:
            return self._max(x.lchild)

        y = x.parent
        while y is not None and x == y.lchild:
            x = y
            y = y.parent
        return y




class Node(object):
    """Binary search tree node class."""
    _key = None
    _parent = None
    _lchild = None
    _rchild = None
    _data = None

    def __init__(self, key, parent=None, lchild=None, rchild=None, data=None):
        self._key = key
        self._parent = parent
        self._lchild = lchild
        self._rchild = rchild
        self._data = data

    @property
    def key(self):
        return self._key

    @property
    def parent(self):
        return self._parent

    @property
    def lchild(self):
        return self._lchild

    @property
    def rchild(self):
        return self._rchild

    @property
    def data(self):
        return self._data

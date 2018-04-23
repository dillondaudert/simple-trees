
class IntervalTree(object):
    """
    A simple implementation of an interval tree.

    All operations run in O(log n) time.
    """

    class Node(object):

        l_child = None
        r_child = None
        max_val = None
        low = None
        high = None

        def __init__(self, low: int, high: int):
            self.low = low
            self.high = high
            self.max_val = high


    def __init__(self):
        self.root = None

    # insert an interval
    # remove an interval
    # given an interval (x, y), determine if it overlaps with another interval
    #    in the tree.

    def insert(self, low, high):

        prev_node = None
        curr_node = self.root
        new_node = self.Node(low, high)

        # if tree is empty
        if curr_node is None:
            self.root = new_node
            return

        l_child = True
        while curr_node is not None:

            # update max val
            if curr_node.max_val < new_node.high:
                curr_node.max_val = new_node.high

            # move to left or right child
            prev_node = curr_node
            if new_node.low < curr_node.low:
                # move to left subtree
                l_child = True
                curr_node = curr_node.l_child
            else:
                # move to right subtree
                l_child = False
                curr_node = curr_node.r_child

        if l_child:
            # insert into prev_node.l_child
            prev_node.l_child = new_node
        else:
            prev_node.r_child = new_node


    def remove(self, low, high):
        pass

    def overlap(self, low, high):
        """
        Check if interval overlaps with another interval in the tree.
        """

        # if interval overlaps with root, return root

        # if left child of root is not empty and the max_val in left child
        #     is greater than x's low value, move to l child
        # else move to r child


"""
This problem was asked by Google. (MEDIUM)

Given the sequence of keys visited by a postorder traversal of a binary search
tree, rebuild the tree.

For example, given the sequence 2, 4, 3, 8, 7, 5, you should build the
following tree:

    5
  3   7 
 2 4    8


[D B E A F C]
[A B D E C F]


D


"""
import time


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_worst(postorder):
    if len(postorder) == 0:
        return None

    root_val = postorder.pop()
    size = len(postorder)
    root = Tree(root_val)

    while size > 0 and root_val < postorder[size - 1]:
        size -= 1

    root.left = build_tree_worst(postorder[0:size])
    root.right = build_tree_worst(postorder[size:])

    return root


def build_tree_best(postorder):
    def build_tree_helper(postorder, index, key, min, max):
        if index[0] < 0:
            return None

        root = None

        if key > min and key < max:
            root = Tree(key)
            index[0] = index[0] - 1

            if index[0] >= 0:
                root.right = build_tree_helper(
                    postorder, index, postorder[index[0]], key, max)
                root.left = build_tree_helper(
                    postorder, index, postorder[index[0]], min, key)

        return root

    val_min = -2**31
    val_max = 2**31

    # array of one element because we need to keep the same reference throughout the recursion
    index = [len(postorder) - 1]
    return build_tree_helper(postorder, index, postorder[index[0]], val_min, val_max)


def test_build_tree_worst_from_postorder_traversal():
    postorder = [2, 4, 3, 8, 7, 5]
    tree = build_tree_worst(postorder)
    assert tree.val == 5
    assert tree.left.val == 3
    assert tree.left.left.val == 2
    assert tree.left.right.val == 4
    assert tree.right.val == 7
    assert tree.right.right.val == 8


def test_build_tree_best_from_postorder_traversal():
    postorder = [2, 4, 3, 8, 7, 5]
    tree = build_tree_best(postorder)
    assert tree.val == 5
    assert tree.left.val == 3
    assert tree.left.left.val == 2
    assert tree.left.right.val == 4
    assert tree.right.val == 7
    assert tree.right.right.val == 8


def test_time_solution():
    postorder = list(range(950))

    start_best = time.time()
    build_tree_best(postorder)
    end_best = time.time()

    start_worst = time.time()
    build_tree_worst(postorder)
    end_worst = time.time()

    assert (end_best - start_best) < (end_worst - start_worst)


"""
SOLUTION:
n = len(postorder)

BEST: O(n)
WORST: O(n^2)
"""

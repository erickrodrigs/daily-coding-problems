"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string back
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

import json


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if root == None:
        return ""

    serialized = dict()
    serialized['val'] = root.val

    left = serialize(root.left)
    if left != "":
        serialized['left'] = left

    right = serialize(root.right)
    if right != "":
        serialized['right'] = right

    return json.dumps(serialized)


def deserialize(s):
    if s == "":
        return None

    tree = json.loads(s)
    root = Node(tree['val'])

    if 'left' in tree:
        root.left = deserialize(tree['left'])

    if 'right' in tree:
        root.right = deserialize(tree['right'])

    return root


def test_serialize_deserialize():
    root = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(root)).left.left.val == 'left.left'


"""
SOLUTION:
n = number of tree nodes

Obs: assuming json.loads and json.dumps are O(1), which actually they're not.

serialize(root):
- time complexity: O(n)

deserialize(root):
- time complexity: O(n)
"""

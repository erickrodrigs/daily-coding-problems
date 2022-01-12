from src.problem003 import Node, serialize, deserialize


def test_serialize_deserialize():
    root = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(root)).left.left.val == 'left.left'

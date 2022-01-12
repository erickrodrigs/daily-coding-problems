from utils.linked_list import LinkedList
from src.problem169 import sort_linked_list


def test_sort_linked_list():
    items = [4, 1, -3, 99]
    linked_list = LinkedList.create(items)
    linked_list.head = sort_linked_list(linked_list.head)

    assert str(linked_list) == "-3 -> 1 -> 4 -> 99"

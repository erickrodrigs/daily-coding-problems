from utils.linked_list import LinkedList
from src.problem177 import rotate_list


def test_for_empty_list():
    linked_list = LinkedList()

    linked_list.head = rotate_list(linked_list.head, 9)

    assert str(linked_list) == ""


def test_when_list_size_is_one():
    linked_list = LinkedList.create([7])

    linked_list.head = rotate_list(linked_list.head, 1)

    assert str(linked_list) == "7"


def test_when_k_is_smaller_than_list_size():
    linked_list = LinkedList.create([1, 2, 3, 4, 5])

    linked_list.head = rotate_list(linked_list.head, 3)

    assert str(linked_list) == "3 -> 4 -> 5 -> 1 -> 2"

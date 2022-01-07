from utils.linked_list import LinkedList
from src.problem169 import sort_linked_list


def test_sort_linked_list():
    setattr(LinkedList, 'sort', sort_linked_list)

    linked_list = LinkedList()
    linked_list.append(4)
    linked_list.append(1)
    linked_list.append(-3)
    linked_list.append(99)

    linked_list.sort()

    assert linked_list.to_string() == "-3 -> 1 -> 4 -> 99"

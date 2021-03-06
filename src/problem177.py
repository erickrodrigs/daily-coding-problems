"""
This problem was asked by Airbnb. (EASY)

Given a linked list and a positive integer k, rotate the list to the right by
k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should
become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should
become 3 -> 4 -> 5 -> 1 -> 2
"""
from utils.linked_list import LinkedList


def size_list(head):
    node = head
    count = 0

    while node != None:
        count += 1
        node = node.next

    return count


def get_last_node(head):
    last_node = head

    while last_node.next != None:
        last_node = last_node.next

    return last_node


def rotate_list(linked_list, k):
    size = size_list(linked_list)

    if size == 0:
        return

    last_node = get_last_node(linked_list)
    node = linked_list
    previous = None

    for _ in range(size - k):
        previous = node
        node = node.next

    new_head = node

    if previous != None:
        previous.next = None

    if linked_list != last_node:
        last_node.next = linked_list

    return new_head


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


"""
SOLUTION:
- time complexity: O(n)
- space complexity: O(1)
"""

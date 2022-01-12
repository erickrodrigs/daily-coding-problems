"""
This problem was asked by Google. (Medium)

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99
"""
from utils.linked_list import LinkedList


def sort_linked_list(linked_list):
    def merge(list_a, list_b):
        head = None
        node = None
        node_a, node_b = list_a, list_b

        while node_a and node_b:
            tmp = None

            if node_a.data < node_b.data:
                tmp = node_a
                node_a = node_a.next
            else:
                tmp = node_b
                node_b = node_b.next

            tmp.next = None

            if node == None:
                node = tmp
                head = tmp
            else:
                node.next = tmp
                node = node.next

        if node_a:
            node.next = node_a
        if node_b:
            node.next = node_b

        return head

    def merge_sort(head):
        if head == None or head.next == None:
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = slow.next
        slow.next = None

        list_a = merge_sort(left)
        list_b = merge_sort(right)

        return merge(list_a, list_b)

    return merge_sort(linked_list)


def test_sort_linked_list():
    items = [4, 1, -3, 99]
    linked_list = LinkedList.create(items)
    linked_list.head = sort_linked_list(linked_list.head)

    assert str(linked_list) == "-3 -> 1 -> 4 -> 99"

from utils.linked_list import LinkedList, LinkedNode


class TestLinkedNode:
    def test_create_a_valid_node(self):
        node = LinkedNode(2, LinkedNode(3))
        assert node.data == 2
        assert node.next.data == 3
        assert node.next.next == None


class TestLinkedList:
    class TestAppend:
        def test_when_list_is_empty(self):
            list = LinkedList()
            list.append(2)
            assert str(list) == "2"

        def test_when_list_has_at_least_one_item(self):
            list = LinkedList.create([1, 2, 3])
            assert str(list) == "1 -> 2 -> 3"

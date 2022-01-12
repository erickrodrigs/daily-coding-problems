class LinkedNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def create(lst):
        linked_list = LinkedList()

        for item in lst:
            linked_list.append(item)

        return linked_list

    def append(self, data):
        new_node = LinkedNode(data)
        node = self.head

        if node == None:
            self.head = new_node
            return

        while node.next != None:
            node = node.next

        node.next = new_node

    def __str__(self):
        node = self.head
        string = ""

        if node != None:
            string += str(node.data)
            node = node.next

        while node != None:
            string += " -> "
            string += str(node.data)
            node = node.next

        return string

    def to_list(self):
        lst = []
        node = self.head

        while node != None:
            lst.append(node.data)
            node = node.next

        return lst

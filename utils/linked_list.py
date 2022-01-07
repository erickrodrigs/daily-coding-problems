class LinkedNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def first(self):
        return self.head

    def append(self, data):
        new_node = LinkedNode(data)
        node = self.head

        if node == None:
            self.head = new_node
            return

        while node.next != None:
            node = node.next

        node.next = new_node

    def to_string(self):
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

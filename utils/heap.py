class EmptyHeapException(Exception):
    def __init__(self, message='the heap is empty'):
        self.message = message
        super().__init__(self.message)


class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        index = len(self.heap) - 1
        parent = self.parent(index)

        while index > 0 and self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            index = parent
            parent = self.parent(parent)

    def delete_min(self):
        size = len(self.heap)

        if size == 0:
            raise EmptyHeapException()

        if size == 1:
            return self.heap.pop()

        value = self.heap[0]
        self.heap[0] = self.heap[size - 1]
        self.heap.pop()
        self.heapify(0)

        return value

    def min(self):
        if len(self.heap) == 0:
            raise EmptyHeapException()

        return self.heap[0]

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def heapify(self, index):
        left = self.left(index)
        right = self.right(index)
        smallest = index
        size = len(self.heap)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(smallest, index)
            self.heapify(smallest)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap)

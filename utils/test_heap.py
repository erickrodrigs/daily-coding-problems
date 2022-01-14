from utils.heap import Heap, EmptyHeapException
import pytest


class TestHeap:
    @pytest.fixture()
    def heap(self):
        heap = Heap()
        heap.insert(4)
        heap.insert(14)
        heap.insert(2)
        heap.insert(6)
        heap.insert(3)
        heap.insert(1)

        return heap

    def test_insert(self, heap):
        assert str(heap) == '[1, 3, 2, 14, 6, 4]'

    def test_min(self, heap):
        assert heap.min() == 1

    def test_min_throwing_exception_when_its_empty(self):
        heap = Heap()
        with pytest.raises(EmptyHeapException):
            heap.min()

    def test_delete_min(self, heap):
        assert heap.delete_min() == 1
        assert heap.min() == 2
        assert str(heap) == '[2, 3, 4, 14, 6]'

    def test_delete_min_throwing_exception_when_its_empty(self):
        heap = Heap()
        with pytest.raises(EmptyHeapException):
            heap.delete_min()

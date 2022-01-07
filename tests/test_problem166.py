import pytest
from src.problem166 import Iterator, NoMoreElementsException


class TestIterator:
    class TestNext:
        def test_raises_exception_when_there_are_no_elements(self):
            iterator = Iterator([])
            with pytest.raises(NoMoreElementsException):
                iterator.next()

        def test_returns_the_correct_element(self):
            iterator = Iterator([[1, 2], [3], [], [4, 5, 6]])
            expected = [1, 2, 3, 4, 5, 6]

            for expect in expected:
                assert iterator.next() == expect

    class TestHasNext:
        def test_returns_false_when_there_are_no_elements(self):
            tests = [Iterator([]), Iterator([[], [], []])]

            for iterator in tests:
                assert iterator.has_next() == False

        def test_returns_true_when_there_are_elements(self):
            tests = [
                [[], [2]],
                [[2, 3], [4, 5]],
                [[2], []]
            ]

            for array in tests:
                iterator = Iterator(array)
                assert iterator.has_next() == True

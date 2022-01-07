from src.problem165 import get_smaller_elements_to_the_right


def test_basic_case():
    assert get_smaller_elements_to_the_right(
        [3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]


def test_with_descending_array():
    assert get_smaller_elements_to_the_right([4, 3, 2, 1]) == [3, 2, 1, 0]


def test_with_ascending_array():
    assert get_smaller_elements_to_the_right(
        [1, 2, 3, 3, 5, 6]) == [0, 0, 0, 0, 0, 0]

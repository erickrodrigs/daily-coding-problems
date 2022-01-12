from src.problem155 import majority_element


def test_find_majority_element():
    lst = [1, 2, 1, 1, 3, 4, 1]
    assert majority_element(lst) == 1

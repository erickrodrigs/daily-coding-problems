from src.problem164 import find_duplicate


def test_find_duplicate():
    tests = [
        {"array": [4, 1, 5, 6, 3, 2, 4, 7], "expected": 4},
        {"array": [1, 1, 2, 3, 4, 5], "expected": 1},
        {"array": [2, 4, 5, 1, 3, 2, 6], "expected": 2}
    ]

    for test in tests:
        array, expected = test["array"], test["expected"]
        assert find_duplicate(array) == expected

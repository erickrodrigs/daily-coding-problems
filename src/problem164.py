"""
This problem was asked by Google. (MEDIUM)

You are given an array of length n + 1 whose elements belong
to the set {1, 2, ..., n}. By the pigeonhole principle,
there must be a duplicate. Find it in linear time and space.
"""


def find_duplicate(arr):
    set_of_numbers = set()

    for number in arr:
        if number in set_of_numbers:
            return number

        set_of_numbers.add(number)


def test_find_duplicate():
    tests = [
        {"array": [4, 1, 5, 6, 3, 2, 4, 7], "expected": 4},
        {"array": [1, 1, 2, 3, 4, 5], "expected": 1},
        {"array": [2, 4, 5, 1, 3, 2, 6], "expected": 2}
    ]

    for test in tests:
        array, expected = test["array"], test["expected"]
        assert find_duplicate(array) == expected


"""
SOLUTION:
- time: O(n)
- space: O(n)
"""

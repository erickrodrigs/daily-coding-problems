"""
This problem was asked by Google. (MEDIUM)

You are given an array of length n + 1 whose elements belong
to the set {1, 2, ..., n}. By the pigeonhole principle,
there must be a duplicate. Find it in linear time and space.
"""


def find_duplicate(arr):
    n = len(arr) - 1
    expected_sum = (n + 1) * n / 2
    actual_sum = sum(arr)
    return actual_sum - expected_sum


"""
SOLUTION:
- time: O(n)
- space: O(1)
"""

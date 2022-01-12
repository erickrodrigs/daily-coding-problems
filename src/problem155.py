"""
This problem was asked by MongoDB. (MEDIUM)

Given a list of elements, find the majority element, which appears
more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""
from math import floor


def majority_element(lst):
    frequency = dict()

    for number in lst:
        if number not in frequency:
            frequency[number] = 0

        frequency[number] += 1

    for (key, value) in frequency.items():
        if value > floor(len(lst) / 2.0):
            return key

    return None


"""
SOLUTION:
n = len(lst)

- time complexity: O(n)
- space complexity: O(n)
"""

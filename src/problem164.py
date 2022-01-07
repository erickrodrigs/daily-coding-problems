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


"""
SOLUTION:
- time: O(n)
- space: O(n)
"""

"""
This problem was asked by Amazon. (EASY)

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""


def gcd(a, b):
    rest = a % b

    while rest != 0:
        a = b
        b = rest
        rest = a % b

    return b


def gcd_list(numbers):
    if len(numbers) == 1:
        return numbers[0]

    return gcd(numbers[0], gcd_list(numbers[1:]))


def test_gcd_list():
    assert gcd_list([42, 56, 14]) == 14


"""
SOLUTION:
n = len(numbers)

- time complexity: O(n * log(min(a, b))), where
a = numbers[i] and b = numbers[i+1] for 0 <= i < n - 1

"""

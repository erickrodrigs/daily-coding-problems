"""
This problem was recently asked by Google. (EASY)

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def has_two_numbers(numbers, k):
    numbers_set = set()

    for num in numbers:
        if (k - num) in numbers_set:
            return True

        numbers_set.add(num)

    return False


def test_has_two_numbers():
    assert has_two_numbers([10, 15, 3, 7], 17) == True


def test_does_not_have_two_numbers():
    assert has_two_numbers([10, 15, 3, 7], 5) == False


"""
SOLUTION:
n = len(numbers)

- time complexity: O(n)
- space complexity: O(n)
"""

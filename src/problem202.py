"""
This problem was asked by Palantir. (EASY)

Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
"""


def palindrome_integer(num):
    copy_num = num
    magnitude = 1

    while copy_num != 0:
        copy_num //= 10

        if copy_num != 0:
            magnitude *= 10

    multiple_of_10 = 1

    while multiple_of_10 < magnitude:
        digit_a = (num // magnitude) % 10
        digit_b = (num // multiple_of_10) % 10

        if digit_a != digit_b:
            return False

        magnitude //= 10
        multiple_of_10 *= 10

    return True


def test_when_integer_is_palindrome():
    assert palindrome_integer(121) == True
    assert palindrome_integer(888) == True
    assert palindrome_integer(1221) == True


def test_when_integer_is_not_palindrome():
    assert palindrome_integer(678) == False


"""
SOLUTION:
n = number of digits of the integer

time: O(n)
space: O(1)
"""

"""
This problem was asked by Amazon. (EASY)

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to
form racecar, which is a palindrome. daily should return false, since
there's no rearrangement that can form a palindrome.
"""


def permutation_of_palindrome(string):
    frequency = {}

    for char in string:
        if not frequency.get(char):
            frequency[char] = 1
        else:
            frequency[char] += 1

    if len(string) % 2 == 0:
        for value in frequency.values():
            if value % 2 != 0:
                return False

        return True
    else:
        only_one_odd = False

        for value in frequency.values():
            if value % 2 != 0:
                if only_one_odd:
                    return False

                only_one_odd = True

        return True


def test_when_is_not_permutation_of_palindrome():
    assert permutation_of_palindrome("daily") == False


def test_when_is_permutation_of_palindrome():
    assert permutation_of_palindrome("carrace") == True


"""
SOLUTION:
n = len(string)

- time complexity: O(n)
- space complexity: O(n)
"""

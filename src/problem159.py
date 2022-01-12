"""
This problem was asked by Google. (EASY)

Given a string, return the first recurring character in it,
or null if there is no recurring character.

For example, given the string "acbbac", return "b".
Given the string "abcdef", return null.
"""


def first_recurring_character(string):
    characters = set()

    for char in string:
        if char in characters:
            return char

        characters.add(char)

    return None


def test_when_there_is_no_recurring_character():
    string = "abcdef"
    assert first_recurring_character(string) == None


def test_find_first_recurring_character():
    string = "acbbac"
    assert first_recurring_character(string) == "b"


"""
SOLUTION:
n = len(string)

- time complexity: O(n)
- space complexity: O(n)
"""

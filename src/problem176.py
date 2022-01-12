"""
This problem was asked by Bloomberg. (EASY)

Determine whether there exists a one-to-one character mapping
from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we
can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot
map to two characters.
"""


def exist_character_mapping(s1, s2):
    if len(s1) != len(s2):
        return False

    map_characters = dict()

    for i in range(len(s1)):
        if s1[i] in map_characters and map_characters[s1[i]] != s2[i]:
            return False

        map_characters[s1[i]] = s2[i]

    return True


"""
SOLUTION:
n = len(s1) = len(s2)
- time complexity: O(n)
- space complexity: O(n)
"""

"""
This problem was asked by Amazon. (HARD)

Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""


def longest_substring(s, k):
    longest = ""

    for i in range(len(s) - k + 1):
        substr = s[i:i+k]
        characters = set(list(substr))

        for j in range(i + k, len(s)):
            if s[j] not in characters and len(characters) == 2:
                break

            characters.add(s[j])
            substr += s[j]

        if len(characters) == 2 and len(substr) > len(longest):
            longest = substr

    return longest


def test_longest_substring():
    assert longest_substring(s="abcba", k=2) == "bcb"
    assert longest_substring(s="aabca", k=2) == "aab"


def test_when_string_does_not_have_longest_substring():
    assert longest_substring(s="aaaaa", k=2) == ""


"""
SOLUTION
n = len(s)

- time complexity: O((n - k) * n)
- space complexity: O((n - k) * n)
"""

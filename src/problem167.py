"""
This problem was asked by Airbnb. (HARD)

Given a list of words, find all pairs of unique indices such that the
concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return
[(0, 1), (1, 0), (2, 3)]
"""


def find_pairs_of_palindromes(list):
    def compare_two_words(word_a, word_b):
        concatenated_word = word_a + word_b
        reversed_concatenated = concatenated_word[::-1]
        return concatenated_word == reversed_concatenated

    pairs = []

    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if compare_two_words(list[i], list[j]):
                pairs.append((i, j))
            if compare_two_words(list[j], list[i]):
                pairs.append((j, i))

    return pairs


"""
SOLUTION:
- let a and b the lengths of the two longest words in the array of length n.
So, the time complexity is O(n^2 len(a + b))
- the space complexity is O(n^2)
"""

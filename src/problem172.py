"""
This problem was asked by Dropbox. (MEDIUM)

Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every
word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"],
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since
there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""


def find_all_starting_indices(s, words):
    if len(words) == 0:
        return []

    frequency = dict()
    starting_indices = []
    number_of_words = len(words)
    word_length = len(words[0])
    total_of_characters = word_length * number_of_words

    if total_of_characters > len(s):
        return []

    for word in words:
        if frequency.get(word):
            frequency[word] += 1
        else:
            frequency[word] = 1

    for i in range(len(s) - total_of_characters + 1):
        tmp_frequency = dict(frequency)
        counter = number_of_words

        for j in range(i, i + total_of_characters, word_length):
            word = s[j:j+word_length]
            print(word)

            if tmp_frequency.get(word) == None or tmp_frequency.get(word) == 0:
                break

            tmp_frequency[word] -= 1
            counter -= 1

        if counter == 0:
            starting_indices.append(i)

    return starting_indices


"""
SOLUTION:
- time complexity: O((s - k)*k)
- space complexity: O((s - k)*n)

where
- s is the length of string s
- k is the total characters of the list of words
- n is the length of the list of words
"""

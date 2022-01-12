"""
HARD

Find an efficient algorithm to find the smallest distance (measured in number
of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of
"dog cat hello cat dog dog hello cat world", return 1 because there's only one
word "cat" in between the two words.
"""


def smallest_distance(text, word_a, word_b):
    last_word_a, last_word_b = -1, -1
    smallest = -1

    for index, word in enumerate(text.split()):
        if word == word_a:
            last_word_a = index
        elif word == word_b:
            last_word_b = index

        if last_word_a != -1 and last_word_b != -1:
            current_distance = abs(last_word_a - last_word_b) - 1

            if smallest == -1 or current_distance < smallest:
                smallest = current_distance

    if last_word_a == -1 or last_word_b == -1:
        return None

    return smallest


"""
SOLUTION:
n = number of words in text

- time complexity: O(n)
- space complexity: O(1)
"""

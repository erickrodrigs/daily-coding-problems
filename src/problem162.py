"""
This problem was asked by Square. (MEDIUM)

Given a list of words, return the shortest unique prefix of each word.
For example, given the list: ["dog", "cat", "apple", "apricot", "fish"]
Return the list: ["d", "c", "app", "apr", "f"]
"""

# assuming list of words is valid, i.e, all words are different of each other


def shortest_unique_prefix(word_list):
    if len(word_list) == 0:
        return []

    all_words = set(word_list)
    prefix_length_count = 1
    are_all_words_prefixed = False
    prefixes = {}  # word -> [its_original_index, its_prefix]

    for i in range(len(word_list)):
        prefixes[word_list[i]] = [i, ""]

    while not are_all_words_prefixed:
        words_by_prefix = {}

        for word in all_words:
            prefix = word[:prefix_length_count]

            if not words_by_prefix.get(prefix):
                words_by_prefix[prefix] = [word]
            else:
                words_by_prefix[prefix].append(word)

        are_all_words_prefixed = True

        for prefix in words_by_prefix.keys():
            if len(words_by_prefix[prefix]) > 1:
                are_all_words_prefixed = False
                continue

            word = words_by_prefix[prefix][0]
            prefixes[word][1] = prefix
            all_words.remove(word)

        prefix_length_count += 1

    result = ["" for i in range(len(word_list))]
    for [index, prefix] in prefixes.values():
        result[index] = prefix

    return result


def test_find_shortest_unique_prefix():
    tests = [
        {
            "word_list": ["dog", "cat", "apple", "apricot", "fish"],
            "expected": ["d", "c", "app", "apr", "f"]
        },
        {
            "word_list": ["zebra", "dog", "duck", "dove"],
            "expected": ["z", "dog", "du", "dov"]
        }
    ]

    for test in tests:
        word_list, expected = test["word_list"], test["expected"]

    assert shortest_unique_prefix(word_list) == expected


"""
SOLUTION:
n = len(word_list)

- time complexity: O(n * len(longest_word)), since we do an
internal loop for all words until they are all prefixed, which
can be done len(longest_word) times. All other loops inside the
'while loop' of the line 24 are linear and the other internal
operations are done in constant time (accessing dictionary and set)

- space complexity: O(n * len(longest_word))
"""

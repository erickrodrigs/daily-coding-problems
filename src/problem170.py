"""
This problem was asked by Facebook. (Medium)

Given a start word, an end word, and a dictionary of valid words,
find the shortest transformation sequence from start to end such that
only one letter is changed at each step of the sequence, and each
transformed word exists in the dictionary. If there is no possible
transformation, return null. Each word in the dictionary have the same
length as start and end and is lowercase.

For example, given start = "dog", end = "cat", and
dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"},
return null as there is no possible transformation from dog to cat.
"""

from collections import deque


def possible_adjacent_words(word, target, dictionary, queue, previous):
    for j in range(len(word)):
        for char in "abcdefghijklmnopqrstuvwxyz":
            new_word = word[0:j] + char + word[j+1:]

            if new_word in dictionary:
                queue.append(new_word)
                dictionary.remove(new_word)
                previous[new_word] = word

                if new_word == target:
                    return True

    return False


def breadth_first_search(start, end, dictionary):
    previous = {}
    queue = deque([start])
    end_bfs = False

    while len(queue) > 0 and not end_bfs:
        length = len(queue)

        for _ in range(length):
            current_word = queue.popleft()
            result = possible_adjacent_words(
                current_word, end, dictionary, queue, previous)

            if result:
                end_bfs = True
                break

    if not end_bfs:
        return None

    return previous


def find_shortest_transformation_sequence(start, end, word_list):
    dictionary = set(word_list)

    if end not in dictionary:
        return None

    previous = breadth_first_search(start, end, dictionary)

    if previous == None:
        return None

    shortest_sequence = [end]
    current_word = end

    while current_word != start:
        current_word = previous[current_word]
        shortest_sequence.append(current_word)

    return shortest_sequence[::-1]


def test_when_there_is_no_possible_transformation():
    tests = [
        {"start": "dog", "end": "cat", "word_list": [
            "dot", "tod", "dat", "dar"]},
        {
            "start": "hit",
            "end": "cog",
            "word_list": ["hot", "dot", "dog", "lot", "log"],
        },
        {
            "start": "hit",
            "end": "cog",
            "word_list": ["hot", "cog"],
        },
    ]

    for test in tests:
        start, end, word_list = test["start"], test["end"], test["word_list"]
        assert find_shortest_transformation_sequence(
            start, end, word_list) == None


def test_return_the_shortest_trasformation():
    tests = [
        {
            "start": "dog",
            "end": "cat",
            "word_list": ["dot", "dop", "dat", "cat"],
            "expected": ["dog", "dot", "dat", "cat"],
        },
        {
            "start": "hit",
            "end": "cog",
            "word_list": ["hot", "dot", "dog", "lot", "log", "cog"],
            "expected": ["hit", "hot", "dot", "dog", "cog"],
        },
    ]

    for test in tests:
        start, end, word_list = test["start"], test["end"], test["word_list"]
        expected = test["expected"]
        assert find_shortest_transformation_sequence(
            start, end, word_list) == expected


"""
SOLUTION:
time complexitiy: O(m^2 * n)
    m = length of a word, n = total of words

space complexity: O(m^2 * n)
"""

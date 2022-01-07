from src.problem170 import find_shortest_transformation_sequence


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

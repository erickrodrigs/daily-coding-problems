from src.problem162 import shortest_unique_prefix


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

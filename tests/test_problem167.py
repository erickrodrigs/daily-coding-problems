from src.problem167 import find_pairs_of_palindromes


def test_when_there_are_no_pairs_of_palindromes():
    list = ["abc", "def", "ghi"]
    expected = []
    assert find_pairs_of_palindromes(list) == expected


def test_when_there_are_pairs_of_palindromes():
    list = ["code", "edoc", "da", "d"]
    expected = [(0, 1), (1, 0), (2, 3)]
    assert find_pairs_of_palindromes(list) == expected

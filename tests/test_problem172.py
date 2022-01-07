from src.problem172 import find_all_starting_indices


def test_when_there_are_no_substrings():
    s = "barfoobazbitbyte"
    words = ["dog", "cat"]
    assert find_all_starting_indices(s, words) == []


def test_return_all_start_indices():
    s = "dogcatcatcodecatdog"
    words = ["cat", "dog"]
    starting_indices = find_all_starting_indices(s, words)
    starting_indices.sort()
    assert starting_indices == [0, 13]

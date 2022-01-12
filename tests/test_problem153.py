from src.problem153 import smallest_distance


def test_find_smallest_distance():
    assert not smallest_distance("hello", "hello", "world")
    assert smallest_distance("hello world", "hello", "world") == 0
    assert smallest_distance(
        "dog cat hello cat dog dog hello cat world", "hello", "world") == 1
    assert smallest_distance(
        "dog cat hello cat dog dog hello cat world", "dog", "world") == 2

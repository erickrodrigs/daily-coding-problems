from src.problem001 import has_two_numbers


def test_has_two_numbers():
    assert has_two_numbers([10, 15, 3, 7], 17) == True


def test_does_not_have_two_numbers():
    assert has_two_numbers([10, 15, 3, 7], 5) == False

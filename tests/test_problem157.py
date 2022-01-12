from src.problem157 import permutation_of_palindrome


def test_when_is_not_permutation_of_palindrome():
    assert permutation_of_palindrome("daily") == False


def test_when_is_permutation_of_palindrome():
    assert permutation_of_palindrome("carrace") == True

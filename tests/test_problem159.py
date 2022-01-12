from src.problem159 import first_recurring_character


def test_when_there_is_no_recurring_character():
    string = "abcdef"
    assert first_recurring_character(string) == None


def test_find_first_recurring_character():
    string = "acbbac"
    assert first_recurring_character(string) == "b"

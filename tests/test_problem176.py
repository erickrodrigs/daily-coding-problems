from src.problem176 import exist_character_mapping


def test_when_there_exists_character_mapping():
    assert exist_character_mapping("abc", "bcd") == True


def test_when_there_is_no_character_mapping():
    assert exist_character_mapping("foo", "bar") == False

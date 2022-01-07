from src.problem173 import flat_dictionary


def test_flat_dictionary():
    dictionary = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }
    expected = {
        "key": 3,
        "foo.a": 5,
        "foo.bar.baz": 8
    }

    assert flat_dictionary(dictionary) == expected

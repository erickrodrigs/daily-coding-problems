"""
This problem was asked by Stripe. (EASY)

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}

You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""


def flat_dictionary_helper(root_key, dictionary, flatten):
    for key in dictionary.keys():
        new_key = key

        if root_key != "":
            new_key = root_key + "." + key

        if type(dictionary[key]) is dict:
            flat_dictionary_helper(new_key, dictionary[key], flatten)
        else:
            flatten[new_key] = dictionary[key]


def flat_dictionary(dictionary):
    flatten_dict = dict()
    flat_dictionary_helper("", dictionary, flatten_dict)
    return flatten_dict


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


"""
SOLUTION:
n = total of keys in dictionary and nested dictionary

- time complexity: O(n)
- space complexity: O(n)
"""

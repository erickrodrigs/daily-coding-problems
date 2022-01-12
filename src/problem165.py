"""
This problem was asked by Google. (MEDIUM)

Given an array of integers, return a new array where each element in the
new array is the number of smaller elements to the right of that element
in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

  There is 1 smaller element to the right of 3
  There is 1 smaller element to the right of 4
  There are 2 smaller elements to the right of 9
  There is 1 smaller element to the right of 6
  There are no smaller elements to the right of 1

"""


def get_smaller_elements_to_the_right(arr):
    answer = []

    for i in range(len(arr)):
        count_smaller = 0

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                count_smaller += 1

        answer.append(count_smaller)

    return answer


def test_basic_case():
    assert get_smaller_elements_to_the_right(
        [3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]


def test_with_descending_array():
    assert get_smaller_elements_to_the_right([4, 3, 2, 1]) == [3, 2, 1, 0]


def test_with_ascending_array():
    assert get_smaller_elements_to_the_right(
        [1, 2, 3, 3, 5, 6]) == [0, 0, 0, 0, 0, 0]


"""
SOLUTION:
- time: O(n^2)
- space: O(n)
"""

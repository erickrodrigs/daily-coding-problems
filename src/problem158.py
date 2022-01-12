"""
This problem was asked by Slack. (MEDIUM)

You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1
represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:

    Right, down, down, right
    Down, right, down, right

The top left corner and bottom right corner will always be 0
"""


def valid_position(i, j, matrix):
    return i >= 0 and j >= 0 and matrix[i][j] == 0


def count_helper(curr_i, curr_j, matrix, ways):
    if curr_i == 0 and curr_j == 0:
        return ways

    valid_top = valid_position(curr_i-1, curr_j, matrix)
    valid_left = valid_position(curr_i, curr_j-1, matrix)

    if valid_top and valid_left:
        ways *= ways
        count_top = count_helper(curr_i-1, curr_j, matrix, ways)
        count_left = count_helper(curr_i, curr_j-1, matrix, ways)
        return count_top + count_left

    if valid_top:
        return count_helper(curr_i-1, curr_j, matrix, ways)

    if valid_left:
        return count_helper(curr_i, curr_j-1, matrix, ways)

    return 0


def count_ways_to_reach_the_bottom_right_corner(matrix):
    end_i = len(matrix)
    end_j = len(matrix[0])
    return count_helper(end_i - 1, end_j - 1, matrix, 1)


def test_count_ways_to_reach_bottom():
    matrix = [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 0]
    ]
    assert count_ways_to_reach_the_bottom_right_corner(matrix) == 7


"""
SOLUTION:
- time complexity: O(2^(n * m))
"""

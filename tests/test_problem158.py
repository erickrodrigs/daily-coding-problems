from src.problem158 import count_ways_to_reach_the_bottom_right_corner


def test_count_ways_to_reach_bottom():
    matrix = [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 0]
    ]
    assert count_ways_to_reach_the_bottom_right_corner(matrix) == 7

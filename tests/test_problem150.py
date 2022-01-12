from src.problem150 import find_nearest_points


def test_find_nearest_points():
    points = [(0, 0), (5, 4), (3, 1)]
    central = (1, 2)
    k = 2
    assert find_nearest_points(points, central, k) == [(0, 0), (3, 1)]

"""
This problem was asked by LinkedIn. (HARD)

Given a list of points, a central point, and an integer k,
find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)],
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)]
"""


def distance(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def find_nearest_points(points, central, k):
    if k >= len(points):
        return points

    points.sort(key=lambda p: distance(p, central))

    return points[:k]


"""
SOLUTION:
n = number of points

- time complexity: O(n lg n)
- space complexity: O(1)

"""

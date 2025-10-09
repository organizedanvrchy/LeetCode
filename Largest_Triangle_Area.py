from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # Helper Function For Using Shoelace Formula
        def area(x, y, z):
            shoelace = abs(x[0] * (y[1] - z[1]) +
                           y[0] * (z[1] - x[1]) +
                           z[0] * (x[1] - y[1])
                          ) * 0.5
            return shoelace

        # Using Combinations
        max_area = 0
        for x, y, z in combinations(points, 3):
            max_area = max(max_area, area(x, y, z))
        return max_area

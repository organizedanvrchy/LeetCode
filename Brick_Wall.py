from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = defaultdict(int)

        for row in wall:
            widthSum = 0
            for brick in row[:-1]:
                widthSum += brick
                edges[widthSum] += 1

        maxEdges = max(edges.values(), default = 0)

        return len(wall) - maxEdges

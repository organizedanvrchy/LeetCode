class UnionFind:
    def __init__(self, n):
        # Initialize parent and rank arrays
        self.parent = list(range(n + 1))
        self.rank = [0] * (n +1)
    
    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        rootX = self.find(x)
        rootY = self.find(y)

        # If x and y are in same set, they form a cycle
        if rootX == rootY:
            return False

        # Attack smaller rank tree under root of higher rank tree
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        for u, v in edges:
            # If union fails, then (u, v) is a redundant edge
            if not uf.union(u, v):
                return [u, v]
    
        return []

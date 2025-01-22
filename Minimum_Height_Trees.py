from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        # Build the adjacency list
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # Find all the initial leaves
        leaves = deque([node for node in range(n) if len(graph[node]) == 1])

        # Trim the leaves layer by layer
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                neighbor = graph[leaf].pop()  # Remove the edge
                graph[neighbor].remove(leaf)  # Remove the reverse edge
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return list(leaves)

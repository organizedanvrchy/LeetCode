from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.mapDict = {}
        self.visited = set()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        self.mapDict[node.val] = Node(node.val)

        def recurse(node, clone):
            self.visited.add(node.val)                                  # Mark node as visited
            for neighbor in node.neighbors:
                if not neighbor.val in self.mapDict:
                    self.mapDict[neighbor.val] = Node(neighbor.val)     # Create cloned neighbor
                if neighbor.val not in self.visited:
                    recurse(neighbor, self.mapDict[neighbor.val])       # Recurse on unvisited neighbors
                clone.neighbors.append(self.mapDict[neighbor.val])      # Add cloned neighbor to cloned node

        recurse(node, self.mapDict[node.val])                       # Start recursion at initial node

        return self.mapDict[node.val]                               # Return cloned graph

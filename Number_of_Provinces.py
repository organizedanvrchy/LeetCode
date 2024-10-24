# LINK to Question: https://leetcode.com/problems/number-of-provinces/description/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provCount = 0
        
        def dfs(city):
            # Mark city as visited
            visited[city] = True
            # Visit all neighboring cities to current city
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        # Traverse through each city (Explore each cell)
        for city in range(n):
            if not visited[city]:
                dfs(city)               # DFS to mark all connected cities
                provCount += 1          # Increment for each connected city
        
        return provCount


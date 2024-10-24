# LINK to Question: https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check for empty grid
        if not grid:
            return 0
        
        def dfs(grid, start):
            stack = [start]
            while stack:
                # Get current cell coordinates
                i, j = stack.pop() 
                # Skip current cell if it is '0' 
                if grid[i][j] == '0':
                    continue
                # Mark cell as visited by setting to '0'
                grid[i][j] = '0'

                # Explore neighbors and add to stack if they are within boundary and are land ('1')
                if i - 1 >= 0 and grid[i - 1][j] == '1':                  # Up
                    stack.append((i - 1, j))
                if i + 1 < len(grid) and grid[i + 1][j] == '1':           # Down
                    stack.append((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == '1':                  # Left
                    stack.append((i, j - 1))
                if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':        # Right
                    stack.append((i, j + 1))

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If an unvisited island is found
                if grid[i][j] == '1':
                    # Start dfs to mark island
                    dfs(grid, (i, j))
                    # Increment count
                    count += 1

        return count

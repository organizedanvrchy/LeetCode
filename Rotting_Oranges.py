# LINK to Question: https://leetcode.com/problems/rotting-oranges/description/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        count = 0

        # Add all rotten oranges to queue and find count of fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:             # Rotten
                    queue.append((r, c))
                elif grid[r][c] == 1:           # Fresh
                    count += 1
        
        # If no fresh oranges exist, return 0
        if count == 0:
            return 0

        # Use BFS to rot adjacent oranges
        mins = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # [Up, Down, Left, Right]

        while queue:
            mins += 1
            for cells in range(len(queue)):
                r, c = queue.popleft()

                # Explore Neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Check if neighbor is within bounds
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # Check if neighbor is fresh
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2            # Make fresh orange rot
                            count -= 1                  # Decrement fresh count
                            queue.append((nr, nc))      # Add new rotten orange to queue

        return mins - 1 if count == 0 else -1

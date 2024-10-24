# LINK to Question: https://leetcode.com/problems/01-matrix/
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        
        # Initialize a matrix with same size as mat and flag all '1' cells as 'inf' 
        distance = []
        for row in range(rows):
            distance.append([float('inf')] * cols)

        # Enqueue all '0' cells and set distance to '0'
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    distance[row][col] = 0
                    queue.append((row, col))    
        
        
        # BFS directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # [Up, Down, Left, Right]
        
        # BFS
        visited = set(queue)
        while queue:
            r, c = queue.popleft()

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if neighbor is within bounds and was not visited yet
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    if distance[nr][nc] > distance[r][c] + 1:
                        distance[nr][nc] = distance[r][c] + 1       # Update distance if new path is shorter
                        visited.add((nr, nc))                       # Mark as visited
                        queue.append((nr, nc))                      # Enqueue to list for further exploration

        return distance

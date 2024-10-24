# LINK to Question: https://leetcode.com/problems/flood-fill/description/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        start = image[sr][sc]
        
        # Return if starting pixel is already target color, otherwise continue
        if start == color:
            return image
        
        def dfs(r, c):
            # Check if current pixel is out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # Check if current pixel is not starting color
            if image[r][c] != start:
                return
            # Change current pixel color
            image[r][c] = color

            # Recursive through neighboring pixels using DFS
            dfs(r - 1, c)   # Up
            dfs(r + 1, c)   # Down
            dfs(r, c - 1)   # Left
            dfs(r, c + 1)   # Right

        # Initiate dfs on starting pixel
        dfs(sr, sc)
        return image

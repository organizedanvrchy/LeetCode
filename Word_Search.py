# LINK to Question: https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        # Using DFS, start from each cell and explore neighbors.
        # If matching char is found, continue to next char in word 
        # until word is either fully matched or not, then backtrack.
        def dfs(r, c, i):
            # If entire word is matched (base case), return
            if i == len(word):
                return True

            # Check for out of bounds char
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # Check for mismatched char
            if board[r][c] != word[i]:
                return False
            
            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = 'V'

            # Recursively explore neighbors
            explored = (dfs(r - 1, c, i + 1) or         # Up
                        dfs(r + 1, c, i + 1) or         # Down
                        dfs(r, c - 1, i + 1) or         # Left
                        dfs(r, c + 1, i + 1))           # Right

            # Restore current cell's original value
            board[r][c] = temp

            return explored

        # Start exploring from each cell in grid to find word
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False

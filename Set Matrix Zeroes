class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)                                            # rows
        n = len(matrix[0])                                         # columns

        # Variables to track if the first row and first column should be zeroed    
        firstRowZero = any(matrix[0][j] == 0 for j in range(n))    # Check if any element in first row is 0
        firstColZero = any(matrix[i][0] == 0 for i in range(m))    # Check if any element in first column is 0 

        # Use first row and first column to mark zero rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0                               # Mark the first element of the row as 0
                    matrix[0][j] = 0                               # Mark the first element of the column as 0
        
        # Zero out columns based on markers
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0        
        
        # Zero out rows based on markers
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        
        # Zero out the first column if needed
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0

        # Zero out the first row if needed
        if firstRowZero:
            for j in range(n):
                matrix[0][j] = 0
        
        return matrix

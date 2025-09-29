class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # Find distance between i and j
        for dist in range(2, n):  # Must have at least 3 vertices
            for x in range(n - dist):
                y = x + dist
                dp[x][y] = float("inf")
                for z in range(x + 1, y):
                    dp[x][y] = min(dp[x][y], dp[x][z] + dp[z][y] + values[x] * values[y] * values[z])

        return dp[0][n - 1]

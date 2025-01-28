class Solution:
    def climbStairs(self, n: int) -> int:
            if n == 0:
                return 0
            elif n == 1:
                return 1

            # Initialize the base cases
            dp = [0] * (n + 1)
            dp[0] = 1  # 1 way to stay at the ground (do nothing)
            dp[1] = 1  # 1 way to reach the first step

            # Fill the dp array using the recurrence relation
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]

            # The result is the number of ways to reach the top (dp[n])
            return dp[n]

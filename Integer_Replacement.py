# Given a positive integer n, you can apply one of the following operations:
# If n is even, replace n with n / 2.
# If n is odd, replace n with either n + 1 or n - 1.
# Return the minimum number of operations needed for n to become 1.

class Solution:
    def integerReplacement(self, n: int) -> int:
        # Use dictionary to store results of subproblem
        memo = {}

        def check(n):
            # Check base case if n is already 1
            if n == 1:
                return 0
    
            # Check for n in the dictionary to avoid redundancy
            if n in memo:
                return memo[n]

            # Check for even/odd cases 
            if n % 2 == 0:
                # If even, integer divide n by 2 and add 1 for current operation
                memo[n] = 1 + check(n//2)
            else:
                # If odd, either add 1 or subtract 1; whichever results in the
                # least total operations 
                memo[n] = 1 + min(check(n+1), check(n-1))

            return memo[n]

        return check(n)

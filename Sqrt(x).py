class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        # Newton's Method
        # Initial Guess
        estimate = x

        while True:
            new_estimate = (estimate + x / estimate) / 2
            # Convergence check
            if abs(new_estimate - estimate) < 1e-7:
                break
            estimate = new_estimate

        # Convert estimate into an integer
        return int(estimate)

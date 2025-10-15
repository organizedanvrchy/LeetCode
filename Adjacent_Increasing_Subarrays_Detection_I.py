class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2 * k:
            return False

        # Helper function to check subarray for strictly increasing elements
        def is_increasing(start):
            for i in range(start, start + k - 1):
                # Check if current number is larger than or same as next number
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        # Check all possible adjacent subarray pairs
        for a in range(n - 2 * k + 1):
            b = a + k
            if is_increasing(a) and is_increasing(b):
                return True

        return False

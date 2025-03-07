class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            # Initialize maximum jump position reachable
            max_jump = 0

            for i in range(len(nums)):
                # If unable to reach index i, return False
                if i > max_jump:
                    return False
                
                # Update maximum jump position
                max_jump = max(max_jump, i + nums[i])

                # If last index is reachable, return True
                if max_jump >= len(nums) - 1:
                    return True
            
            # If loop is completed, last index was reached.
            return True

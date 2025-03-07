class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Already at last index, no jumps needed
        if n == 1:
            return 0

        jumps = 0
        curr_max_jump = 0
        next_max_jump = 0

        for i in range(n - 1):
            # Update maximum reach of jump
            next_max_jump = max(next_max_jump, i + nums[i])
            
            # Check if a new jump is needed
            if i == curr_max_jump:
                jumps += 1
                # Move to next jump range
                curr_max_jump = next_max_jump
                # Check if the last index is reached
                if curr_max_jump >= n - 1:
                    return jumps

        return jumps

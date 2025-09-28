class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Sort array
        nums.sort()

        # Fix z as largest possible side
        for z in range(len(nums) - 1, 1, -1):
            y = z - 1   # second largest possible side
            x = z - 2   # third largest possible side
            
            # Apply triangle inequality to find valid
            # triangle sides. In this case, first triangle
            # found should have largest perimeter already.
            if nums[x] + nums[y] > nums[z]:
                perimeter = (nums[x] + nums[y] + nums[z])
                return perimeter
        
        return 0

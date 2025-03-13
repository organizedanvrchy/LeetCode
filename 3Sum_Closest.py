class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort nums before using two-pointer approach
        nums.sort()
        
        n = len(nums)
        closest_sum = float("inf")

        # Iterate through array while fixing one number at a time
        # and using two pointers to find the closest sum
        for i in range(n - 2):
            beginning = i + 1
            end = n - 1

            while beginning < end:
                current_sum = nums[i] + nums[beginning] + nums[end]

                # Update closest sum
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # If current sum is less than target, 
                # then move beginning pointer to the right
                if current_sum < target:
                    beginning += 1
                # If current sum is greater than target
                # then move end pointer to the left
                elif current_sum > target:
                    end -= 1
                # Else, if the exact target sum is found
                # return immediately
                else:
                    return current_sum      
                    
        return closest_sum


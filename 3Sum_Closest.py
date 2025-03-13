class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        n = len(nums)
        closest_sum = float("inf")

        for i in range(n - 2):
            beginning = i + 1
            end = n - 1

            while beginning < end:
                current_sum = nums[i] + nums[beginning] + nums[end]

                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    beginning += 1
                elif current_sum > target:
                    end -= 1
                else:
                    return current_sum      

        return closest_sum


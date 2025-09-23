class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums) - 2):
            # Check if sum of first and third num
            # equals exactly half of second num
            if (nums[i] + nums[i + 2]) == (nums[i + 1] / 2):
                count += 1

        return count

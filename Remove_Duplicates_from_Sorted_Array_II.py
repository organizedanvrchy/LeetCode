class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        count_ptr = 2 
        for i in range(2, len(nums)):
            if nums[i] != nums[count_ptr - 2]:
                nums[count_ptr] = nums[i]
                count_ptr += 1
        return count_ptr

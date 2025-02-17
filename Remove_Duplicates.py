class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        k = 1

        for n in range(1, l):
            if nums[n] != nums[n - 1]:
                nums[k] = nums[n]
                k += 1

        return k

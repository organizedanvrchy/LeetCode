class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = len(nums)
        k = 0

        for num in range(l):
            if nums[num] != val:
                nums[k] = nums[num]
                k += 1
        
        return k

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        
        if n == 0:
            return 0

        # Use a fast pointer, i, to iterate through array
        for i in range(1, n):
            # If a unique element is found
            if nums[i] != nums[k]:
                k += 1
                # Move unique element forward
                nums[k] = nums[i]

        # Add 1 to k, since k is index-based
        return k + 1
                
        

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Sort array in ascending order 
        # (easier for triangle inequality -- 
        # sum of the two smaller sides must 
        # be greater than the largest side)
        nums.sort()
        arr_len = len(nums)
        triplet_count = 0

        # Fix largest side to k and iterate 
        # from n - 1 to 2
        for k in range(arr_len - 1, 1, -1):
            i = 0
            j = k - 1
            # Use two pointer method to find pairs of i
            # and j that satisfy triangle inequality
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    triplet_count += (j - i)
                    j -= 1
                else:
                    i += 1
                    
        return triplet_count
        


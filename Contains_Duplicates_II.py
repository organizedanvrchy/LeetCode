# Initial Solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen_index_dict = {}

        for i, num in enumerate(nums):
            if num in last_seen_index_dict and i - last_seen_index_dict[num] <= k:
                return True
            last_seen_index_dict[num] = i

        return False

# Optimized Solution
# from typing import List

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         # Step 1: If all elements are unique, return False immediately
#         if len(set(nums)) == len(nums):
#             return False
        
#         # Step 2: Iterate through each index and check if a duplicate exists in the next k elements
#         for i in range(0, len(nums)):
#             if nums[i] in nums[i+1:i+k+1]:  # Look in the slice from i+1 to i+k
#                 return True
        
#         # Step 3: If no duplicates are found within k distance, return False
#         return False

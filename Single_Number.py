class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num

# Alternate solution (XOR)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         xor = 0
#         for num in nums:
#             xor ^= num
        
#         return xor

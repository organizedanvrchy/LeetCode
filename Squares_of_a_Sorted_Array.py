# LINK to Question: 

def sortedSquares(self, nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    
    left = 0
    right = len(nums) - 1
    
    pos = len(nums) - 1
    
    while left <= right:
        leftSquare = nums[left] ** 2
        rightSquare = nums[right] ** 2
        
        if leftSquare > rightSquare:
            res[pos] = leftSquare
            left += 1
        
        else:
            res[pos] = rightSquare
            right -= 1
            
        pos -= 1
        
    return res

"""
Alt Attempt:

def sortedSquares(nums):
    squared_nums = [num ** 2 for num in nums]
    squared_nums.sort()
    return squared_nums

This is slower [O(nlogn)] and uses a bit more space than two-pointer method [O(n)]
"""

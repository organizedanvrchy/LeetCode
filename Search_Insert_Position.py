# Initial Solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for num in range(len(nums)):
            if nums[num] == target:
                i = nums.index(target)
                return i
            
            if target not in nums:
                nums.append(target)
                nums.sort()
                i = nums.index(target)
                return i

# Expected Solution
# Binary Search
left, right = 0, len(nums) - 1

while left <= right:
    # Get middle element of array
    mid = (left + right) // 2
    # If target is found in middle of array, return its index
    if nums[mid] == target:
        return mid
    # If target is less than middle element, search left half of array
    elif nums[mid] < target:
        left = mid + 1
    # Otherwise, target is more than middle element, search right hald of array
    else:
        right = mid - 1

# If no target is found in array, return position where it should be inserted
return left

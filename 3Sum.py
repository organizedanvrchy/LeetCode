class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip same element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two-pointer method
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for 2nd and 3rd elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1

                    # Move pointers
                    left += 1
                    right -= 1

                elif curr_sum < 0:
                    # If the sum is too small, move the left pointer to the right
                    left += 1

                else:
                    # If the sum is too large, move the right pointer to the left
                    right -= 1

        return result

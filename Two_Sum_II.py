class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Pointer to first element
        left = 0
        # Pointer to last element
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[left] + numbers[right]

            if curr_sum == target:
                # Convert to 1-based index
                return [left + 1, right + 1]
            elif curr_sum < target:
                # Move to right and increase sum
                left += 1
            else:
                # Move to left and decrease sum
                right -= 1

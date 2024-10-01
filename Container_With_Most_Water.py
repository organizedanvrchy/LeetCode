# LINK to Question: https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area, using height of shorter column & distance between columns
            area = min(height[left], height[right]) * (right - left)
            # Update the maximum area
            max_area = max(max_area, area)
            
            # Move the pointer with the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

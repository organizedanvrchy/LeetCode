# LINK to Question: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Check if array is empty (base case)
        if not nums:
            return None

        # Find middle element index
        midIndex = len(nums) // 2

        # Since array is sorted, use middle element as root node
        root = TreeNode(nums[midIndex])

        # Recursively build left and right subtrees
        root.left = self.sortedArrayToBST(nums[:midIndex])
        root.right = self.sortedArrayToBST(nums[midIndex+1:])

        return root

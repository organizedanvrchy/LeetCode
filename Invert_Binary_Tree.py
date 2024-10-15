# LINK to Question: https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If tree or subtree is empty, return None
        if not root:
            return None

        # Swap left and right children
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return root after inverting subtrees
        return root

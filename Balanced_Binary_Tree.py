# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Get height of tree and return height of subtree if balanced
        def height(node):
            if not node:
                return 0    # Tree height of 0 is balanced
            
            # Recursively get height of left and right subtrees
            leftSub = height(node.left)
            rightSub = height(node.right)

            # If either subtree is not balanced, move -1 up thr tree
            if leftSub == -1 or rightSub == -1:
                return -1

            # If the current node is not balanced, return -1
            if abs(leftSub - rightSub) > 1:
                return -1
            
            # Return the height of the subtree rooted at current node
            return max(leftSub, rightSub) + 1

        # Tree is balanced if height() does not return -1
        return height(root) != -1

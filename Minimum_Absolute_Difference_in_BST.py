# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # In-order traversal using stack
        stack = []
        curr = root
        prev_val = None
        min_diff = float('inf')

        while stack or curr:
            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Calculate min_diff with previous value
            if prev_val is not None:
                min_diff = min(min_diff, curr.val - prev_val)

            prev_val = curr.val

            # Move to right child
            curr = curr.right
        
        return min_diff


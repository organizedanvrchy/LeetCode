# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to traverse tree in Post-Order
        # and prune the tree
        def prune(node):
            if not node:
                return None
            
            # Recursively check left child then right child
            node.left = prune(node.left)
            node.right = prune(node.right)

            # Since node.val is either 0 or 1, if node.val is 0 and
            # both children are None, prune current node
            if node.val == 0 and not node.left and not node.right:
                return None
            
            return node
        
        # Return modified root of tree
        return prune(root)

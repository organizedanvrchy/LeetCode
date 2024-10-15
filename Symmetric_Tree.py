# LINK to Question: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirrorImage(tree1: TreeNode, tree2: TreeNode) -> bool:
            # If both trees are None, 
            # they are mirror images
            if not tree1 and not tree2:
                return True
            # If one is None and the other is not, 
            # they are not mirror images
            if not tree1 or not tree2:
                return False
            
            # Return true if current nodes have same value 
            # and the subtrees are mirrors of each other
            return (tree1.val == tree2.val and
                    mirrorImage(tree1.left, tree2.right) and
                    mirrorImage(tree1.right, tree2.left))

        # Return true if right and left subtree
        # are mirror images of each other.
        return mirrorImage(root, root)

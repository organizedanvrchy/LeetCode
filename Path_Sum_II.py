# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            # Add the current node's value to the path and update the sum
            current_path.append(node.val)
            current_sum += node.val
            
            # Check if it's a leaf node and the path sum matches the target
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(current_path))
            else:
                # Recurse on the left and right subtrees
                dfs(node.left, current_path, current_sum)
                dfs(node.right, current_path, current_sum)
            
            # Backtrack to explore other paths
            current_path.pop()
        
        result = []
        dfs(root, [], 0)
        return result

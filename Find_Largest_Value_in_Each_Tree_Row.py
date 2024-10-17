# LINK to Question: https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # Check for empty tree
        if not root:
            return []
        
        # Create queue for BFS (level order traversal)
        queue = deque([root])
        res = []

        while queue:
            # Get length of current row
            rowLength = len(queue)
            # Initialize max value for current row
            maxVal = float('-inf')

            # Traverse nodes in current level
            for nodes in range(rowLength):
                node = queue.popleft()
                maxVal = max(maxVal, node.val)

                # Recursively check if left and right children exist 
                # and add them to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append max value for current level to res array
            res.append(maxVal)
            
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Check for empty tree
        if not root:
            return 0

        # Create queue to hold tuple (node, current depth)
        queue = deque([(root, 1)])

        # Using BFS to search level by level and
        # stop when it a leaf node is found
        while queue:
            node, depth = queue.popleft()

            # Check for leaf nodes
            if not node.left and not node.right:
                return depth
            
            # Add left child to queue if it exists
            if node.left:
                queue.append((node.left, depth + 1))

            # Add right child to queue if it exists
            if node.right:
                queue.append((node.right, depth + 1))

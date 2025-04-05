# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = deque([root])

        while queue:
            # Number of nodes at current level
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # If current node is last node in current level
                # Append to resultant array
                if i == level_size - 1:
                    res.append(node.val)

                # Add children to queue for next level, 
                # if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return res

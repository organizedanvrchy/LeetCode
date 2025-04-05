# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        # Initialize resultant array and double ended queue
        # to process nodes level by level (BFS)
        res = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                # Pop nodes from queue (current level)
                node = queue.popleft()

                # Calculate sum of nodes in current level
                level_sum += node.val

                # Add left child to queue, if they exist
                if node.left:
                    queue.append(node.left)
                
                # Add right child to queue, if they exist
                if node.right:
                    queue.append(node.right)

            # Find average and append to resultant array
            ave = level_sum / level_count
            res.append(ave)

        return res

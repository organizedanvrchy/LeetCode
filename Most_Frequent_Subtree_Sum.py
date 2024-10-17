# LINK to Question: https://leetcode.com/problems/most-frequent-subtree-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # Dictionary to store frequency of subtree sums
        treeSumFreq = defaultdict(int)
        
        # Helper adder function to calculate subtree sums
        def adder(node):
            # Check if tree is empty (base case)
            if not node:
                return 0
            
            # Calculate sum of current subtree recursively
            leftSum = adder(node.left)
            rightSum = adder(node.right)
            total = node.val + leftSum + rightSum

            # Update frequency count
            treeSumFreq[total] += 1

            return total
        
        # Calculate subtree sums starting from root
        adder(root)

        # Find max frequency
        if not treeSumFreq:
            return []

        maxFreq = max(treeSumFreq.values())

        # Return all sums that equal the max frequency
        return [s for s, count in treeSumFreq.items() if count == maxFreq]

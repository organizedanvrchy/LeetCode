# LINK to Question: https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # This method "deletes" the current node by 
        # copying the value of the next node into the
        # current node and links to the next node's next, 
        # essentially skipping over the next node.
        node.val = node.next.val        # Copy value from next node to current node
        node.next = node.next.next      # Link current node to next node's next

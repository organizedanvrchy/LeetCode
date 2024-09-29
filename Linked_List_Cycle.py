# LINK to Question: https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize fast/slow pointers for Floyd's Cycle Detection Algorithm
        slow = head
        fast = head

        # Traverse List
        while fast is not None and fast.next is not None:
            slow = slow.next            # Move slow pointer one step forward
            fast = fast.next.next       # Move fast pointer two steps forward

            # Check whether slow and fast pointers meet
            # and if they do, a cycle is present 
            if slow == fast:
                return True

        # Otherwise, no cycle detected
        return False

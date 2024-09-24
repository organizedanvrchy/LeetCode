# LINK to Question: https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if list is empty, only one node long, or if k = 0 (no rotation)
        if not head or not head.next or k == 0:
            return head

        # Get length of list and connect tail to head to form a circular list
        l = 1
        tail = head
        while tail.next:          # Move tail to end of list
            tail = tail.next
            l += 1
        tail.next = head          # Point tail to head to form a circular list
  
        # Normalize k in case it is greater than the length of the list 
        k = k % l

        # Find new tail position and rotate list
        newHeadPos = l - k                      # Get position of new head node at rotation
        newTail = head                          # Start from original head of the list
        for _ in range(newHeadPos - 1):         # Move newTail pointer to node just before new head
            newTail = newTail.next 

        # Break circular list
        newHead = newTail.next
        newTail.next = None

        return newHead

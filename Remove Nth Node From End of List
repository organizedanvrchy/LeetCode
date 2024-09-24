# LINK to Question: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create temp head for edge cases (such as deleting head)
        temp = ListNode(0)
        temp.next = head
        first = temp
        second = temp

        # Move first n+1 steps ahead of second to ensure gap is 
        # n nodes apart
        for _ in range(n+1):
            first = first.next

        # Move both pointers forward until first reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Second should be at the node before the nth node and the 
        # nth node is then skipped
        second.next = second.next.next

        return temp.next

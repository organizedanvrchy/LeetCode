# LINK to Question: https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create temp nodes to start two lists
        lowerHead = ListNode(0)
        higherHead = ListNode(0)

        # Create pointers to the two lists
        lower = lowerHead
        higher = higherHead

        # Traverse original list
        current = head
        while current:
            if current.val < x:
                lower.next = current        # Append to the lower list
                lower = lower.next
            else:
                higher.next = current       # Append to the higher list
                higher = higher.next
            current = current.next

        # Connect the two lists
        higher.next = None                  # Terminate higher list
        lower.next = higherHead.next        # Connect lower list tail to  
                                            # head of higher list

        # Return new head
        return lowerHead.next

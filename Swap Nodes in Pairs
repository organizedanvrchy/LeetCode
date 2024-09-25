# LINK to Question: https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to point to head of list,
        # useful for managing edge cases
        temp = ListNode(0)
        temp.next = head
        prev = temp           # temp node placed before head

        while prev.next and prev.next.next:
            first = prev.next          
            second = prev.next.next    

            first.next = second.next   # skip over second node (detaches 'second' from 'first')
            second.next = first        # reverse order of the two nodes (second points to first)
            prev.next = second         # connects new first node in swapped pair to previous part of list

            prev = first               # move prev forward to first for processing next pair, if any

        return temp.next

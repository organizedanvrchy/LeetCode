# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    # Find the end node of the list
    def findTail(self, head):
        tail = head

        # Iterate through list as long as tail is not None
        # and tail.next exists
        while tail and tail.next:
            tail = tail.next
        
        return tail

    # Appends val to the list pointed to by head and returns new head
    def appendToList(self, head, val):
        node = ListNode(val)

        tail = self.findTail(head)

        # If tail is None, new node becomes the head of the list
        # Otherwise, new node is appended to current tail
        if not tail:
            return node
        else:
            tail.next = node
            return head

    def addTwoNumbers(self, l1, l2):
        l3 = None
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0    # If l1 is not None, use its value. Otherwise, use 0. 
            val2 = l2.val if l2 else 0    # Same logic as above.

            res = val1 + val2 + carry
            val = res % 10                # val of current node is the remainder of res divided by 10.
            carry = res // 10             # Carry is the integer division of res by 10.
            
            l3 = self.appendToList(l3, val)

            l1 = l1.next if l1 and l1.next else None    # Move l1 to next node if it exists. Otherwise, set to None.
            l2 = l2.next if l2 and l2.next else None    # Same logic as above.
        
        if carry:
            l3 = self.appendToList(l3, carry)           # Check for remaining carry and append as new node to list

        return l3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Helper Function to Calculate GCD
    def gcd(a, b):
        while b != 0:
            a = b
            b = a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            # Calculate GCD of Current Node and Next Node
            curr_gcd = gcd(temp.val, temp.next.val)
            # Create New Node with GCD Value
            new_node = ListNode(curr_gcd)
            # Insert New Node between Current Node and Next Node
            new_node.next = temp.next
            temp.next = new_node
            # Move to Next Pair of Nodes
            temp = new_node.next
        
        return head

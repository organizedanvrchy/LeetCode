# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = []
        
        # Add values in list1 to new list
        while list1:
            merged_list.append(list1.val)
            list1 = list1.next
        
        # Add values in list2 to the same new list
        while list2:
            merged_list.append(list2.val)
            list2 = list2.next
        
        # Sort the new list (Most time and memory consuming portion of code)
        merged_list.sort()

        # Convert list to linked list
        temp = ListNode()
        current = temp
        for i in merged_list:
            current.next = ListNode(i)
            current = current.next

        # Return head of new linked list
        return temp.next

# Alternative Approach (Pointers Only - O(n+m) space efficiency and O(1) memory efficiency)
        # # Dummy node to simplify edge cases
        # dummy = ListNode()
        # # Pointer to build the new list
        # current = dummy     
        
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         current.next = list1
        #         list1 = list1.next
        #     else:
        #         current.next = list2
        #         list2 = list2.next
        #     # Move to the newly added node
        #     current = current.next  
        
        #     # Append the remaining part of the non-empty list
        #     current.next = list1 if list1 else list2

        #     # Return the merged list starting from the first real node
        #     return dummy.next  

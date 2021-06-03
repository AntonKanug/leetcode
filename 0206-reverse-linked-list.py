# https://leetcode.com/problems/reverse-linked-list/submissions/
# easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    tempHead = None
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        # Helper function for recursion
#         def helper(curr, prev):
#             if curr.next != None:
#                 helper(curr.next, curr)
#             else:
#                 self.tempHead = curr
                        
#             curr.next = prev
#             if prev: prev.next = None
        
#         helper(head, None)
#         return self.tempHead

        # Iterative
        newhead = None
    
        while(head):
            temp2 = ListNode(head.val, head.next)
            temp2.next = newhead
         
            newhead = temp2
            
            head = head.next
            
        return newhead
      
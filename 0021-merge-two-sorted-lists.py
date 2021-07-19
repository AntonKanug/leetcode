# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        res = ListNode()
        temp = res
        
        while(l1 and l2):
            if l1.val < l2.val:
                temp.next = ListNode(l1.val, None)
                l1 = l1.next                
            else:
                temp.next = ListNode(l2.val, None)
                l2 = l2.next
            temp = temp.next
            
        nonEmpty = l1 if l1 else l2
        
        while(nonEmpty):
            temp.next = ListNode(nonEmpty.val, None)
            temp = temp.next
            nonEmpty = nonEmpty.next
            
        return res.next

# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        
        # Init pointers
        turt = head
        if head.next and head.next.next: hare = head.next.next
        else: return False

        while(turt != hare):
            turt = turt.next
            if hare.next: hare = hare.next.next
            else: return False
            
            if not hare or not turt: return False
            
        return True
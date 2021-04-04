# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if (not k or not head or not head.next): 
            return head
        
        len = 1
        tail = head
        newHead = head
        temp = head

        while (tail.next):
            len+=1
            tail = tail.next
        
        if (not k%(len)):
            return head
        
        newTail = temp
        for i in range(len-k%(len)-1):
            newHead = newHead.next
            temp = temp.next

        newHead = newHead.next
        temp.next = None
        tail.next = newTail
        
        return newHead
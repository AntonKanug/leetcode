# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
# Time - O(n)
# Space - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        lenList = 0
        while(temp):
            temp = temp.next
            lenList+=1

        # Creating empty temp head
        head = ListNode(0,head)
        temp = head
    
        for i in range(lenList-n):
            temp = temp.next
        
        if temp.next and temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None

        return head.next
    
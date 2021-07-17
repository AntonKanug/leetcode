# https://leetcode.com/problems/add-two-numbers/submissions/
# Time - O(max(m,n))
# Space - O(max(m,n)) output, else O(1)

# Idea:
# Add l1 and l2 in and keep iterating
# Keep a pointer to last (temp) and second last pointer (prev)
# If l1 and l2 len diff => add the non empty linked list
# At end if carry => temp.val = carry, else => prev.next = None
# Return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        temp = head
        prev = None

        carry = 0
        while(l1 and l2):
            tempSum = l1.val + l2.val + carry
            carry = tempSum // 10
            tempSum = tempSum % 10
            
            prev = temp
            temp.val = tempSum
            temp.next = ListNode()
            temp = temp.next
            
            l1, l2 = l1.next, l2.next
        
        nonEmpty = l1 if l1 else l2
        
        while(nonEmpty):
            tempSum = nonEmpty.val + carry
            carry = tempSum // 10
            tempSum = tempSum % 10
            
            prev = temp
            temp.val = tempSum
            temp.next = ListNode()
            temp = temp.next
            
            nonEmpty = nonEmpty.next
                
        if carry: temp.val = carry
        else: prev.next = None

        return head
    

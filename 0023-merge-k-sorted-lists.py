# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp = []
        for i in lists:
            x = i
            while x:
                temp.append(x.val)
                x = x.next
    
        heapq.heapify(temp)
        res = ListNode()
        cur = res
        
        while temp:
            cur.next = ListNode(heapq.heappop(temp), None)
            cur = cur.next
            
        return res.next
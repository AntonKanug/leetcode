# https://leetcode.com/problems/minimum-cost-to-connect-sticks/submissions/

import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        
        for i in range(len(sticks)-1):
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            
            cost += x+y
            
            heapq.heappush(sticks, x+y)
            
        return cost
        
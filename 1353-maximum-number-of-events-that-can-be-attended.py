# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

from heapq import *

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: -x[0])
        minHeap = []
        d = 0
        c = 0
        
        while minHeap or events:
            # If no events need to be attended get next/current day
            if not minHeap: d = events[-1][0]
            
            # Add all the current day's ending times
            while events and d == events[-1][0]:
                heappush(minHeap, events.pop()[1])
            # Use an event for today
            heappop(minHeap)
            
            # Remove all events that cannot be atteneded by today
            while minHeap and minHeap[0] == d:
                heappop(minHeap)
            
            d+=1
            c+=1       
            
        return c
    
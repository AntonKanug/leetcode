# https://leetcode.com/problems/employee-free-time/submissions/

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from heapq import *

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap, res = [], []
        
        for i, employee in enumerate(schedule):
            time = employee.pop(0)
            heappush(heap, [time.start, time.end, i])
            
        last_end = heap[0][1]
        
        while heap: 
            start, end, i = heappop(heap)
            
            if start <= last_end:
                last_end = max(end, last_end)
            else:
                res.append(Interval(last_end, start))
                last_end = end
                
            if schedule[i]:
                time = schedule[i].pop(0)
                heappush(heap, [time.start, time.end, i])
        
        return res
    
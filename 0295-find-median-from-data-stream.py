# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap:
            heapq.heappush(self.minHeap, [num, num]) 
            return
        elif num <= self.minHeap[0][1]:
            heapq.heappush(self.maxHeap, [-num, num])
        else: 
            heapq.heappush(self.minHeap, [num, num])
            
        self.balance()
        
    def balance(self):
        if len(self.minHeap) > len(self.maxHeap):
            x = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, [-x[1], x[1]])
            
        elif len(self.minHeap) < len(self.maxHeap):
            x = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, [x[1], x[1]])
        
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.maxHeap[0][1] + self.minHeap[0][1])/ 2
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0][1]
        return self.maxHeap[0][1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# https://leetcode.com/problems/the-skyline-problem/submissions/

from heapq import *

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for x1,x2,y in buildings:
            points.append([x1,y,'s'])
            points.append([x2,y,'e'])
            
        self.heights = []
        self.inHeap = {} # height: inHeap, shouldBeInHeap
        self.pushHeap(0)
        
        points.sort(key=lambda x:x[2],reverse=True)
        points.sort(key=lambda x:-x[1])
        points.sort(key=lambda x:x[0])
        mainPoints = []
        
        for x,y,p in points:
            if p == 's':
                if y > self.getMaxHeap():
                    mainPoints.append([x,y])
                self.pushHeap(y)
            elif p == 'e':
                self.inHeap[y][1]-=1
                if y > self.getMaxHeap():
                    mainPoints.append([x,self.getMaxHeap()])
        
        output = []
        
        for x,y in mainPoints:
            if output and (output[-1][0] == x or output[-1][1] == y):
                output.pop()
            output.append([x,y])
            
        return output
        
        
    def getMaxHeap(self):
        val = -self.heights[0]
        
        while self.inHeap[val][0] != self.inHeap[val][1]:
            self.removeHeap(val)
            val = -self.heights[0]
            
        return val
    
        
    def pushHeap(self, val):
        if val in self.inHeap and self.inHeap[val][1] < self.inHeap[val][0]:
            self.inHeap[val][1] += 1
            return
        elif val in self.inHeap:
            self.inHeap[val][0]+=1
            self.inHeap[val][1]+=1
        else:
            self.inHeap[val] = [1,1]
        heappush(self.heights,-val)
            
            
    def removeHeap(self, val):
        if self.heights[0] == -val:
            self.inHeap[val][0] -= 1
            heappop(self.heights)
            
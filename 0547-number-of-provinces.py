# https://leetcode.com/problems/number-of-provinces/submissions/

from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        toVisit = deque()
        visited = set()
        count = 0
        
        for z in range(len(isConnected)):
            if z not in visited: toVisit.append(z)
                
            while toVisit:
                i = toVisit.popleft()
                arr = isConnected[i]

                if i not in visited: count +=1 
                visited.add(i)

                for j, val in enumerate(arr):
                    if val and j not in visited:
                        visited.add(j)
                        toVisit.append(j)
        return count
                
# https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        
        q = deque()
        q.append((0,0,1))
        grid[0][0] = -1
        
        while q:
            i,j,d = q.popleft()
            
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return d
            
            for x,y in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
                x1,y1 = x+i,y+j

                if not(0<=x1<len(grid) and 0<=y1<len(grid[0])): continue
                if grid[x1][y1] == 0:
                    q.append((x1,y1,d+1))
                    grid[x1][y1] = -1

        return -1
    
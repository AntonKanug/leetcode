# https://leetcode.com/problems/shortest-path-to-get-food/

from collections import deque

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        x,y = 0,0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '*': x,y = i,j
                    
        q = deque()
        visited = set()
        
        # x,y,len
        q.append([x,y,0])
        
        while q:
            i,j,l = q.popleft()
            
            if (i,j) in visited: continue
 
            visited.add((i,j))
            
            if not(0 <= i < len(grid) and 0 <= j < len(grid[0])): continue
            
            if grid[i][j] == '#': return l
            if grid[i][j] == 'X': continue
             
            for m,n in [[0,1],[1,0],[-1,0],[0,-1]]:
                if (i+m,j+n) not in visited:
                    q.append([i+m,j+n,l+1])
            
        return -1
    
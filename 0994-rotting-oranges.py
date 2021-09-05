# https://leetcode.com/problems/rotting-oranges/submissions/

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        maxMin = 0        
        oranges = 0
        rotten = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    oranges +=1
                elif grid[i][j] == 2:
                    # [x,y,minute]
                    q.append([i,j,0])
                    rotten+=1
        
        while q:
            i,j,m = q.popleft()
            
            if (i,j) in visited: continue
            
            visited.add((i,j))
            maxMin = max(maxMin,m)
            
            for ver,hor in [[0,1],[1,0],[0,-1],[-1,0]]:
                x,y = i+ver, j+hor
                if not(0<=x<len(grid) and 0<=y<len(grid[0])): continue
                if (x,y) not in visited and grid[x][y] == 1:
                    q.append([x,y,m+1])
        
        return maxMin if len(visited)-rotten == oranges else -1

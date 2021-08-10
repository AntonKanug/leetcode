# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/submissions/
# m*n*k

from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        dest = (len(grid)-1,len(grid[0])-1)
        q = deque()
        q.append(((0,0), 0, k))
        visited = set((0,0,k))
            
        while q:
            cur, dist, k = q.popleft()
            row, col = cur     
            
            if cur == dest: return dist
            
            for i, j in [(row,col+1), (row+1,col), (row-1, col), (row, col-1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    if k and grid[i][j] and (i, j, k-1) not in visited:
                        visited.add((i, j, k-1))
                        q.append([(i,j), dist+1, k-1])

                    elif not grid[i][j] and (i, j, k) not in visited:
                        visited.add((i, j, k))
                        q.append([(i,j), dist+1, k])
                        
        return -1
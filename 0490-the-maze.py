# https://leetcode.com/problems/the-maze/submissions/

# Idea:
# BFS: at each point go all the way till wall in direction
# We know it stops at a wall => when dest is found => true

from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = deque()
        q.append(start)
        
        while q:
            i,j = q.popleft()

            if [i,j] == destination: return True
                
            for x,y in [[0,1],[1,0],[0,-1],[-1,0,]]:
                x1,y1 = x+i,y+j
                
                while 0<=x1<len(maze) and 0<=y1<len(maze[0]) and not maze[x1][y1]!=1: 
                    x1 += x
                    y1 += y
    
                x1 -= x
                y1 -= y
                
                if not maze[x1][y1]:
                    q.append([x1,y1])
                    maze[x1][y1] = -1
                    
        return False
    
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

import heapq

class Solution:
    grid = []
    tgt = None
    
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        start, tgt, box = None, None, None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S': start = (i,j)
                if grid[i][j] == 'T': tgt = (i,j)
                if grid[i][j] == 'B': box = (i,j)
        self.tgt = tgt
        self.grid = grid
        
        visited = set()
        heap = [[self.dist(start), 0, box, start]]

        while heap:
            _, moves, box, pos = heapq.heappop(heap)

            for i,j in [[0,1],[1,0],[-1,0],[0,-1]]:
                newpos = (pos[0]+i, pos[1]+j)
                newbox = box
                newmoves = moves
                
                if not self.inbound(newpos): continue
                    
                if newpos == box:
                    newbox = (box[0]+i, box[1]+j)
                    if not self.inbound(newbox): continue 
                    newmoves+=1
                    if newbox == tgt: return newmoves
        
                if (newbox,newpos) not in visited:
                    visited.add((newbox,newpos))
                    heapq.heappush(heap,[self.dist(newbox) + newmoves, newmoves, newbox, newpos])

        return -1
    
    
    def dist(self, point):
        return abs(self.tgt[0] - point[0]) + abs(self.tgt[1] - point[1])
    
    def inbound(self, point):
        return 0<=point[0]<len(self.grid) and 0<=point[1]<len(self.grid[0]) \
               and self.grid[point[0]][point[1]] != '#'
               
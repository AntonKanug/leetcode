# https://leetcode.com/problems/making-a-large-island/

class Solution:
    grid = []
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid, sizes = grid, {0:0}
        island, maxs = 2, 0
        
        # DFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 1:
                    self.grid[i][j] = island
                    sizes[island] = self.dfs(i,j, island, 1)
                    maxs = max(maxs, sizes[island])
                    island+=1
                    
        # Go through 0s
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 0:
                    vals = set()
                    for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
                        if self.inrange(x+i,y+j): 
                            vals.add(self.grid[x+i][y+j])

                    size = 1
                    for k in vals:
                        size += sizes[k] 
                    maxs = max(maxs, size)
                    
        return maxs

        
    def dfs(self, i, j, c, s):
        for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
            if self.inrange(x+i,y+j) and self.grid[x+i][y+j] == 1:
                self.grid[x+i][y+j] = c
                s += self.dfs(x+i, y+j, c, 1) 

        return s


    def inrange(self, i, j):
        return 0<=i<len(self.grid) and 0<=j<len(self.grid[0])
    
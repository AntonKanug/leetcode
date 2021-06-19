# https://leetcode.com/problems/number-of-islands/submissions/
# O(m*n) - time
# O(m+n) - space (max recursion depth)

# When 1 found follow all the ones mark -1
# When new 1 found island+=1
# Skip 0 and -1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        islands = 0
        h = len(grid)
        w = len(grid[0])
        
        # Explore island and mark all of it -1
        def explore(i,j):
            # If i or j out of range return
            if i < 0 or i >= h or j < 0 or j >= w:
                return
            # If island is reached or not and island return
            if grid[i][j] == -1 or grid[i][j] == "0":
                return
            
            # Else mark at is part of island
            grid[i][j] = -1
            
            # Explore its neighbours
            for x,y in directions:
                explore(i+x, j+y)
        
        # Go through grid 
        for i in range(h):
            for j in range(w):
                # If island founds -> its new
                if grid[i][j] == "1":
                    # Increment island count and explore the rest
                    islands+=1
                    explore(i,j) 
                
        return islands
                            
                            

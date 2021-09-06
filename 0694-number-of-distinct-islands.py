# https://leetcode.com/problems/number-of-distinct-islands/submissions/

class Solution:
    x,y = 0,0
    grid = []
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.x, self.y = len(grid), len(grid[0])
        self.grid = grid
        paths = set()
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    path = self.explore(i,j)
                    paths.add(path)
                    
        return len(paths)
        
        
    def explore(self,i,j):
        path = ''
        
        for x,y,df,db in [[0,1,'r','l'],[1,0,'d','u'],[0,-1,'l','r'],[-1,0,'u','d']]:
            x1,y1 = i+x, j+y
            
            if not(0<=x1<self.x and 0<=y1<self.y): continue
            if self.grid[x1][y1]==1:
                self.grid[x1][y1] = -1
                # curDirection + path + direction to move back
                path += df + self.explore(x1,y1) + db
                
        return path
    
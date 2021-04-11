# https://leetcode.com/problems/coordinate-with-maximum-network-quality/submissions/
# medium

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        mX, mY= float('inf'), float('inf') 
        MX, MY =  float('-inf'), float('-inf')
        
        for i in towers:
            if i[0] < mX: mX =  i[0]
            if i[0] > MX: MX =  i[0] 
            if i[1] < mY: mY =  i[1] 
            if i[1] > MY: MY =  i[1] 
            
        maxCoords = [0,0]
        maxVal = 0
        
        for i in range(mX,MX+1):
            for j in range(mY,MY+1):
                q = 0
                for k in towers:
                    d = self.getD([i,j], k)
                    
                    if d <= radius:
                        q += int(k[2]/(1+d))
                        
                if q > maxVal:
                    maxCoords = [i,j]
                    maxVal = q
        return maxCoords
                        
                
                
    def getD(self, point1, point2):
        return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5
                
                

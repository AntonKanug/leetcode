# https://leetcode.com/problems/spiral-matrix/submissions/
# Time - O(n)
# Space - O(1) w/o output

# Idea:
# Keep bondaries and complete the a loop
# Once completed move in
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        
        left, right = 0, len(matrix[0])-1
        up, down = 0, len(matrix)-1
        
        while (not left>right and not up>down):
            for i in range(left, right+1):
                output.append(matrix[up][i])
            
            for i in range(up+1, down):
                output.append(matrix[i][right])
                
            if up != down:
                for i in reversed(range(left, right+1)):
                    output.append(matrix[down][i])
                    
            if left!= right:
                for i in reversed(range(up+1, down)):
                    output.append(matrix[i][left])
                
            left+=1
            right-=1
            up+=1
            down-=1
            
        return output
    
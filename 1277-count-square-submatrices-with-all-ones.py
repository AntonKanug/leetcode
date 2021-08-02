# https://leetcode.com/problems/count-square-submatrices-with-all-ones/submissions/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        count = 0
        
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                
                if matrix[i-1][j-1]:
                    count+=1
                    dp[i][j] = 1
                    
                    minVal = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    if minVal > 0:
                        count += minVal
                        dp[i][j] = minVal + 1
                        
        return count
# https://leetcode.com/problems/unique-paths/submissions/
# Time - O(m*n)
# Space - O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[],[]]
        
        dp[0] = [1 for i in range(n)]
        dp[1] = [0 for i in range(n)]
        dp[1][0] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                dp[1][j] = dp[0][j] + dp[1][j-1]
                
            dp[0] = dp[1]
            dp[1] = [0 for i in range(n)]
            dp[1][0] = 1
            
        return dp[0][-1]
        
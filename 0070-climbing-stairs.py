# https://leetcode.com/problems/climbing-stairs/
# Time - O(n)
# Space - O(1)

# dp[i] = dp[i-1] + dp[i-2]
# dp[i-1] + 1 step
# dp[i-2] + 2 steps

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        
        dp = [0, 1, 2]

        for i in range(2, n):
            dp[0], dp[1] = dp[1], dp[2]
            dp[2] = dp[0] + dp[1]
            
        return dp[-1]
        
        

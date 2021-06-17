# https://leetcode.com/problems/coin-change/submissions/

# O(n*m) - Time
# O(m) - space

# Idea:
# Assume dp[i] is the min
# In that case cycle through all the coins find if adding it would require less coing
# -> dp[i-coinValue] + 1 = new coins if we were to include it
# Update dp[i] with the min

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')]*amount
        
        for i in range(1,amount+1):
            for coin in coins:
                if (i - coin >= 0):
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
      

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/

# O(n) - time
# O(1) - space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        gain = 0
        for i in range(len(prices)-1):  
            gain += max(0, prices[i+1]-prices[i])
            
        return gain

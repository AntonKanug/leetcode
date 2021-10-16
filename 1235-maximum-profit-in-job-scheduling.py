# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

# To improve:
# Append when a time is selected
# When finding other profits at start do bin search

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        times = [[p, s, e] for p, s, e in zip(profit, startTime, endTime)]        
        times.sort(key=lambda x: x[-1])
        
        profits = [[0,0]]
        maxp = 0
        
        for p, s, e in times: 
            maxp = max(maxp, p + self.bin_search(profits, s))
            profits.append([maxp, e])
        
        return maxp
    
    
    def bin_search(self, profits, start):
        l, r = 0, len(profits)-1
        
        while l<=r:
            mid = l + (r-l)//2
            
            if profits[mid][1] == start: return profits[mid][0]
            elif profits[mid][1] < start: l = mid + 1
            else: r = mid - 1
                
        return profits[r][0]
    
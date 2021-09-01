# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

# To improve:
# Append when a time is selected
# When finding other profits at start do bin search

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        times = []
        
        for p, s, e in zip(profit, startTime, endTime): times.append([p, s, e])
        
        times.sort(key=lambda x: x[-1])
        
        dpProfit = [0] * (times[-1][2]+1)
        
        j = 0
        
        for i in range(1, len(dpProfit)):
            dpProfit[i] = dpProfit[i-1]
            p, s, e = times[j]
            
            while i == e:
                dpProfit[i] = max(dpProfit[i], dpProfit[s] + p)
                j+=1
                if j < len(times): p, s, e = times[j]
                else: break

        return dpProfit[-1]
    
    
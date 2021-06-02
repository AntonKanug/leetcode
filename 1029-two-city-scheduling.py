# https://leetcode.com/problems/two-city-scheduling/submissions/
# medium

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = 0
        
        for i in costs: i.append(i[0]-i[1])
            
        costs.sort(key=lambda i: i[2])
                
        for i in range(len(costs)):
            if (i < len(costs)//2): cost+=costs[i][0]
            else: cost+=costs[i][1]

        return cost
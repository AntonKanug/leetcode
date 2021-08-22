# https://leetcode.com/problems/analyze-user-website-visit-pattern/submissions/

from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        users = {}
        
        for u, t, w in sorted(zip(username, timestamp, website)):
            if u not in users: users[u] = [w]
            else: users[u].append(w)
                
        counters = {}
        maxV = []
        maxC = float('-inf')
        
        for u in users:
            for i in set(combinations(users[u], 3)):
                if i in counters: counters[i]+=1
                else: counters[i] = 1
                
                if counters[i] > maxC:
                    maxC = counters[i]
                    maxV = [i]
                elif counters[i] == maxC:
                    maxV.append(i)
                    
        return sorted(maxV)[0]
                
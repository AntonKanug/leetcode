# https://leetcode.com/problems/connecting-cities-with-minimum-cost/

import heapq

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        edges = {}
        
        for dest, to, cost in connections:
            if dest in edges: edges[dest].append([cost, to])
            else: edges[dest] = [[cost, to]]
                
            if to in edges: edges[to].append([cost, dest])
            else: edges[to] = [[cost, dest]]
        
        visited = set()
        toVisit = [[0,1]]
        total = 0
        
        while toVisit:
            visit = heapq.heappop(toVisit)
            if visit[1] in visited: continue
                
            total += visit[0]
            visited.add(visit[1])
            
            for to in edges[visit[1]]:
                if to[1] not in visited:
                    heapq.heappush(toVisit, to)
            
        if len(visited) < n: return -1
        
        return total
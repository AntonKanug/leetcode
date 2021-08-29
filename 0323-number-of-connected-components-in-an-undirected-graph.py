# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = {}
        
        for i in range(n):
            connected[i] = set([])

        for fro, to in edges:
            connected[fro].add(to)
            connected[to].add(fro)
                
        visited = set()
        q = deque()
        count = 0

        for i in range(n):
            if i in visited: continue
            
            q.append(i)
            
            while q:
                j = q.popleft()
                if j in visited: continue
                    
                visited.add(j)
                
                for node in connected[j]:
                    if node not in visited:
                        q.append(node)
            count+=1 
            
        return count
        
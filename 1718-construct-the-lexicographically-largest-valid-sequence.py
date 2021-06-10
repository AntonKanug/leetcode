# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/submissions/
# Backtracking
# O(n!) - Time
# O(n) - space

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        output = [0]*((n-1)*2+1)
        visited = [False]*(n+1)
        
        def dfs(i):
            if i == len(output): return True
            
            if output[i]: return dfs(i+1)
        
            for num in range(n,0,-1):
                if visited[num] or ((i+num >= len(output) or output[i+num]!=0) and num!=1): continue
                
                # Assume this num works for positon
                visited[num] = True
                output[i] = num
                if num!=1: output[i+num] = num
                
                # Increment and run dfs
                if dfs(i+1): return True
                
                # If this num doesnt work -> reverse changes and continue
                visited[num] = False
                output[i] = 0
                if num!=1: output[i+num] = 0
                
            return False
                
        dfs(0)
        return output

# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/submissions/
# O(m*n) - Time
# O(max(m,n)) - Space

# Also could be done in DP
# Keep each dir length at each point
# If 1 => add 1 to all 3 directions from the respective items above, left, across
# Return [-1][-1] max of all 3 directions
# O(m*n) - Space

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
        maxLen = 0
        
        # Horizontal
        for i in mat: maxLen = max(maxLen, self.findMaxLen(i))
        
        # Vertical
        for j in range(len(mat[0])):
            temp = []
            for i in mat: temp.append(i[j])
            maxLen = max(maxLen, self.findMaxLen(temp))
        
        # Diag
        for k in range(len(mat[0])):
            toItr = [0]
            if not k: toItr = range(len(mat))
            for j in toItr:
                temp = []
                i = j
                j = k
                while i < len(mat) and j < len(mat[0]):
                    temp.append(mat[i][j])
                    i+=1
                    j+=1
                maxLen = max(maxLen, self.findMaxLen(temp))
                
        # Rev diag
        for k in range(len(mat[0]))[::-1]:
            toItr = [0]
            if k == len(mat[0])-1: toItr = range(len(mat))
    
            for j in toItr:
                temp = []
                i = j
                j = k
                while i < len(mat) and j >= 0:
                    temp.append(mat[i][j])
                    i+=1
                    j-=1
                maxLen = max(maxLen, self.findMaxLen(temp))

        return maxLen
    
    
        
    def findMaxLen(self, arr):
        maxLen = 0
        count = 0
        i = 0
        while i < len(arr):
            if arr[i]: count+=1
            else: count = 0  
            maxLen = max(count, maxLen)
            i+=1
        return maxLen
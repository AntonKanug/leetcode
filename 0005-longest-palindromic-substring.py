# https://leetcode.com/problems/longest-palindromic-substring/submissions/
# O(n^2) - Time
# O(1) - Space

# Idea
# Iterate over each char
# Go outwards from i and find max dist
# In case where len(res) is odd findMax(i,i)
# Else findMax(i,i+1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def findMax(l,r):
            while( l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return (r - l -2 + 1, (l+1,r-1))
        
        maxStr = ''
        
        for i in range(len(s)):
            x = findMax(i, i)
            y = findMax(i, i+1)
            
            maxTemp = y if (x[0] < y[0]) else x
            
            if len(maxStr) < maxTemp[0]:
                maxStr = s[maxTemp[1][0]:maxTemp[1][1]+1]
            
        return maxStr
        

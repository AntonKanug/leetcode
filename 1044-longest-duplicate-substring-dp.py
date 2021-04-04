# https://leetcode.com/problems/longest-duplicate-substring/
# hard - dp version

class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        dp = [[0]*(len(s)+1) for i in range(len(s)+1)]
        
        maxLen = 0
        x = 0
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                if j>i and s[i]==s[j]:
                    dp[i][j]=dp[i-1][j-1]+1
                    
                    if dp[i][j] > maxLen: 
                        maxLen =  dp[i][j]
                        x = i
                        
        if maxLen < 0:
            return ""
        x+=1
        return s[x-maxLen:x]
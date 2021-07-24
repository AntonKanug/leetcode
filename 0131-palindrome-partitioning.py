# https://leetcode.com/problems/palindrome-partitioning/submissions/

# Idea:
# Check if a str palindrome
# If true => str + partition(s[str_idx+1:])
# Optional cache for better time but worse space
class Solution:
            
    def isPalindrome(self, s):
        for i in range(len(s)//2):
            if s[i]!=s[-i-1]: return False
        return True
    
    
    # No cache    
    def partitionNoCache(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        res = []
        
        for i in range(len(s)):
            temp = s[:i+1]
            if self.isPalindrome(temp):
                for j in self.partition(s[i+1:]):
                    res.append([temp] +j)                 
        return res
    
    
    # With cache
    def partition(self, s: str) -> List[List[str]]:
        cache = [[] for _ in range(len(s)+1)]
        
        def helper(s, idx):
            
            if not s: return [[]]
            res = []
            
            for i in range(len(s)):
                if self.isPalindrome(s[:i+1]):
                    # Cache layer
                    if not cache[idx+i+1]:
                        cache[idx+i+1] =  helper(s[i+1:], idx+i+1)
                        
                    for j in cache[idx+i+1]:
                        res.append([s[:i+1]] +j) 
            return res
        
        return helper(s, 0)
           
        
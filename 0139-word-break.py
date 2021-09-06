# https://leetcode.com/problems/word-break/

class Solution:
    cache = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.cache = {}
        
        # Local function for caching
        def wordBreakLocal(s, wordDict):
            for i in range(1,len(s)):
                prefix = s[:i]
                suffix = s[i:]

                if prefix in wordDict:
                    if suffix not in self.cache:
                        self.cache[suffix] = wordBreakLocal(suffix, wordDict) 
                    if self.cache[suffix]: return True
           
            return s in wordDict
        
        return wordBreakLocal(s,wordDict)
    
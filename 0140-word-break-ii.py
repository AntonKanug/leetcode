# https://leetcode.com/problems/word-break-ii/

class Solution:
    cache = {}
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.cache = {} 
        return self.wordBreakHelper(s, wordDict)
    
    def wordBreakHelper(self, s: str, wordDict: List[str]) -> List[str]:  
        output = []    

        if s in wordDict: output.append(s)
        
        for i in range(1,len(s)):
            if s[i:] not in self.cache:
                self.cache[s[i:]] = self.wordBreakHelper(s[i:], wordDict)
            if s[:i] in wordDict and self.cache[s[i:]]:
                for word in self.cache[s[i:]]:  
                    output.append(s[:i] + ' ' + word) 

        return output
    
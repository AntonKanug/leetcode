# https://leetcode.com/problems/longest-string-chain/submissions/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cache = {}
        lengths = {}
        maxLen = 0
        maxChain = 1
        
        for word in words:
            cache[word] = 0
            if len(word) in lengths:
                lengths[len(word)].add(word)
            else: lengths[len(word)] = set([word])
            maxLen = max(len(word), maxLen)
    
        # Helper func to do subproblems
        def helper(length, prevWord):
            if length == 0: return 1
            if length-1 not in lengths: return 1
            
            curMax = 1
            
            for word in lengths[length-1]:
                if not cache[word]:
                    cache[word] = helper(length-1, word)
                if self.compareStr(prevWord, word):
                    curMax = max(curMax, cache[word]+1)
                    
            cache[prevWord] = curMax
            
            return curMax
        
        for i in lengths[maxLen]: helper(maxLen, i)
        for i in cache: maxChain = max(maxChain, cache[i])
            
        return maxChain
    
    # str1 > str2
    def compareStr(self, str1, str2):
        i, j = 0, 0
        
        while(j<len(str2) and i<len(str1)):
            if str1[i] == str2[j]:
                i+=1
                j+=1
            else: i+=1
            if i - j == 2: return False
            
        return True
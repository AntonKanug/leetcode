# https://leetcode.com/problems/verifying-an-alien-dictionary/
# O(n*l) - time
# O(1) - space

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if (len(words)==1): return True
        
        alpha = {}
        
        for i,l in enumerate(order):
            alpha[l] = i
        
        def compare(word1, word2):
            for i in range(len(word1)):

                if (i>=len(word2)):  return False
                
                if (alpha[word1[i]] < alpha[word2[i]]): return True
                
                if (alpha[word1[i]] == alpha[word2[i]]): continue
                    
                return False
            
            return True
        
        for i in range(len(words)-1):
            if (not compare(words[i], words[i+1])): return False
        
        return True

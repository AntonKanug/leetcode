# https://leetcode.com/problems/concatenated-words/submissions/

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        output = []
        cache = {}
        
        def helper(word, secondWord):
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in words:
                    if suffix not in cache:
                        cache[suffix] = helper(suffix, True)
                    if cache[suffix]:
                        return True
                
            return secondWord and word in words and word


        for word in words:
            if helper(word, False): output.append(word)
                    
        return list(set(output))
    
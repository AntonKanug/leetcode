# https://leetcode.com/problems/word-ladder/submissions/

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList: return 0
        
        wordList = [beginWord] + wordList
        words = {}
        
        for word in wordList: 
            for i in range(len(word)):
                x = word[:i] + '-' + word[i+1:]
                if x in words:
                    words[x].add(word)
                else:
                    words[x] = set([word])
                    
        q = deque()
        visited = set([])                                
        visited.add(beginWord)        
        
        for i in range(len(beginWord)):
            q.append([beginWord[:i] + '-' + beginWord[i+1:], 1])
        
        while q:
            cur, curc = q.popleft()
            
            if endWord in words[cur]: return curc+1

            if cur in visited: continue
            visited.add(cur)
            
            for word in words[cur]:
                for i in range(len(beginWord)):
                    x = word[:i] + '-' + word[i+1:]
                    if x not in visited:
                        q.append([x,curc+1])

        return 0
    
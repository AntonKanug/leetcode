# https://leetcode.com/problems/sentence-screen-fitting/submissions/

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        row = 0
        words = 0
        lenSent = len(sentence)
        firstWords = {}
        
        while(row < rows):
            firstWord = sentence[words%lenSent]
            
            # If in cache
            if firstWord in firstWords:
                words += firstWords[firstWord]
                row+=1 
                continue
            
            # Else - calculate
            sentCount = 0
            col = 0
            while (col < cols):
                curWordLen = int(bool(col)) * 1 + len(sentence[words%lenSent])
                if col + curWordLen <= cols:
                    col += curWordLen
                    words += 1
                    sentCount += 1
                else: break
             
            firstWords[firstWord] = sentCount
            row+=1 
            
        return words//lenSent
                
# https://leetcode.com/problems/text-justification/submissions/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        wordsByLine = []
        temp = []
        lenWords = 0
        
        # Calculate needs
        for i, word in enumerate(words):
            if len(word) + (i and 1) + lenWords <= maxWidth:
                temp.append(word)
                lenWords += len(word) + (i and 1)
            else:
                wordsByLine.append((temp, maxWidth - lenWords))
                temp = [word]
                lenWords = len(word)
        wordsByLine.append((temp, maxWidth - lenWords))  
        
        
        output = []
        
        # All line but last
        for line in wordsByLine[:-1]:
            temp = line[0][0]
            
            # If one word
            if len(line[0]) == 1:
                output.append(temp + " "*line[1])
                continue

            spacesPerWord = line[1] // (len(line[0])-1)
            spacesLeft = line[1] % (len(line[0])-1)
            
            for word in line[0][1:]:
                if spacesLeft: 
                    temp += " "
                    spacesLeft -=1
                    
                temp +=  " " * (1 + spacesPerWord) + word
            
            output.append(temp)
            
        # Last line
        output.append(" ".join(wordsByLine[-1][0]) + " " * wordsByLine[-1][1])
        
        return output
            
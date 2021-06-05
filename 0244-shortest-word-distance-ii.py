# https://leetcode.com/problems/shortest-word-distance-ii/submissions/
# medium
# O(n) - time
# O(n) - space (for hashmap)

class WordDistance:
    
    def __init__(self, wordsDict: List[str]):
        self.worddict = {}
        for i, w in enumerate(wordsDict):
            if w in self.worddict:
                self.worddict[w].append(i)
            else:
                self.worddict[w] = [i]
        
    def shortest(self, word1: str, word2: str) -> int:
        w1 = self.worddict[word1]
        w2 = self.worddict[word2]
        dist = float('inf')
        
        i, j = 0, 0
        
        while(i!=len(w1) and j!=len(w2)):
            if (abs(w1[i]-w2[j]) < dist):
                dist = abs(w1[i]-w2[j])
    
            if (w1[i] > w2[j]): j+=1
            else: i+=1
        
        # If end of w1 not reached check 1 more 
        if (i<len(w1)-1 and abs(w1[i+1]-w2[j-1]) < dist):
                dist = abs(w1[i+1]-w2[j-1])
                
        # If end of w2 not reached check 1 more 
        elif (j<len(w2)-1 and abs(w1[i-1]-w2[j+1]) < dist):
                dist = abs(w1[i-1]-w2[j+1])
            
        return dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

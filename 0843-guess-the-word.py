# https://leetcode.com/problems/guess-the-word/
# O(n) - time
# O(n) - space
# hard

# P(0) = 80%
# P(1) = 19%
# P(2...6) < 2%
# P(x) = C(n,x) * 1/26 ^ x * (25/26) ^ 6-x

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        for i in range(10):
            
            # Create 6 x 26 size array and hold count of each letter at position
            letterCount = [[0]*26]*6
            for j in wordlist:
                for k,l in enumerate(j):
                    letterCount[k][ord(l)-ord('a')]+=1
            
            # Find the word with most chars at position
            maxScore = 0
            guess = ''
            for j in wordlist:
                score = 0
                for k,l in enumerate(j):
                    score+=letterCount[k][ord(l)-ord('a')]
                if (score>maxScore):
                    guess = j
                    maxScore = score
                    
            # Guess
            count = master.guess(guess)
            
            #If 6 -> found
            if count == 6: return guess
            
            # If not remove word
            wordlist.remove(guess)
            words =  []
            
            # Only keep chars are in same position at least <count> times
            for j in wordlist:
                similarChar = 0
                for k,l in enumerate(j):
                    if (guess[k]==l): similarChar += 1
                        
                if (similarChar == count):
                    words.append(j)
                    
            wordlist = words      
            
                    
            
                    
                    
            
# https://leetcode.com/problems/number-of-matching-subsequences/submissions/
# O(s + len(words)) - Time
# O(words) - Space

# Idea:
# Keep hashmap of all words where key is first letter
# Iterate through s and retrieve all words starting with i
# Remove all words from that key and add them but with str[1:]
# At end only words who couldnt be found will be left
# len(words) - len(left over words in hashmap)

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        letters = {}
        
        def addToLetters(word):
            if not word: return
            if word[0] in letters: letters[word[0]].append(word)
            else: letters[word[0]] = [word]
        
        for word in words: addToLetters(word)
        
        for i in s:
            if i in letters:
                temp = list(letters[i])
                letters[i] = []
                for j in temp:
                    addToLetters(j[1:])
                    
        count = 0
        for i in letters: count += len(letters[i])
            
        return len(words)-count
        

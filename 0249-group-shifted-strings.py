# https://leetcode.com/problems/group-shifted-strings/

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        abc = 'abcdefghijklmnopqrstuvwxyz'
        words = {}
        
        for word in strings:
            new = 'a'

            for letter in word[1:]:
                new += abc[(ord(word[0]) - ord(letter))%26]
                
            if new in words: words[new].append(word)
            else: words[new] = [word]

        output = []     
        for word in words:
            output.append(words[word])
            
        return output
    
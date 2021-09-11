# https://leetcode.com/problems/regular-expression-matching/submissions/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        T = []
        
        # s * p
        for i in range(len(s)+1):
            T.append([0] * (len(p)+1))
            
        T[0][0] = 1
        
        # a*b* case
        for j in range(2,len(p)+1):
            if p[j-1] == '*': T[0][j] = T[0][j-2]
        
        
        for I,i in enumerate(range(1,len(s)+1)):
            for J,j in enumerate(range(1,len(p)+1)):
                
                # if letters equal or pattern is '.' 
                # => these match => get the value without them [i-1][j-1]
                if s[I] == p[J] or p[J] == '.': T[i][j] = T[i-1][j-1]
                    
                # If '*'
                elif p[J] == '*':
                    # If '*' and we dont count the last letter (a*)
                    # Get the value from [_]a*
                    T[i][j] = T[i][j-2] 
                    # If '*' and we do count the last pattern occurence (a*, .*)
                    # Get value from the row above
                    if s[I] == p[J-1] or p[J-1] == '.':
                        T[i][j] |= T[i-1][j]
        
        return T[-1][-1]
    
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        
        def helper(cur, opening, closing):
            
            # If maxlen -> string found
            if opening == n and closing == n: 
                output.append(cur)
                return
            
            # If a string has less than n openings add one
            if opening < n:
                helper(cur+'(', opening+1, closing)
             
            # If a string has more opening that closing add a closing
            if opening > closing:
                helper(cur+')', opening, closing+1)
                
        helper('',0,0)
        
        return output
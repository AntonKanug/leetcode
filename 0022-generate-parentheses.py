# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        
        def helper(cur, opening, closing):
            
            # If maxlen -> string found
            if len(cur) == n*2: 
                output.append(cur)
                return
            
            # If a string has less than n openings add one
            if opening < n:
                cur+='('
                helper(cur, opening+1, closing)
                cur=cur[:-1]
             
            # If a string has more opening that closing add a closing
            if opening > closing:
                cur+=')'
                helper(cur, opening, closing+1)
                cur=cur[:-1]
                
        helper('',0,0)
        
        return output

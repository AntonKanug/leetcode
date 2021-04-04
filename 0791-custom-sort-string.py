# https://leetcode.com/problems/custom-sort-string/submissions/
# medium

class Solution:
    def customSortString(self, S: str, T: str) -> str:
        x = {}
        output = ''
        
        # Create map of letters have
        for i in T:
            if i in x.keys():
                x[i] +=1
            else:
                x[i]=1
        
        # Go through S and add chars
        for i in S:
            if i in x.keys():
                output += i*x[i]
                x.pop(i)
            
        # Add in rest from T
        for i in x.keys():
            output += i*x[i] 
            
        return output                
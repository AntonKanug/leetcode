# https://leetcode.com/problems/remove-comments/submissions/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        skip = False
        skip2 = False
        temp = '\n'.join(source)
        newStr = ''
        i = 0
    
        singleComment = False
        while i < len(temp):
            
            val = temp[i]
            next2 = temp[i:i+2] if i < len(temp) else ''
            
            if not singleComment:
                if next2 == '/*':
                    if skip: skip2 = True
                    skip = True
                if next2 == '*/' and (skip2 or (skip and i > 1 and temp[i-1:i+2] != '/*/')):               
                    skip = False 
                    skip2 = False
                    i+=2
                    continue
                    
            if not skip:
                if next2 == '//':
                    singleComment = True
                elif singleComment and val == '\n':
                    singleComment = False 
                    
            if not skip and not singleComment:
                newStr += val
            i+=1
        
        output = [] 
        for i in newStr.split('\n'): 
            if i: output.append(i)
                
        return output
        
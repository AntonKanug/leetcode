# https://leetcode.com/problems/decode-string/
# medium 

class Solution:
    def decodeString(self, s: str) -> str:
            
        i = 0
        
        while i!= len(s):            
            if s[i] == "[":
                
                j = i+1
                x = 0
                
                # Find end of bracket
                while j!= len(s):
                    if s[j] == "[":
                        x +=1
                    elif s[j] == "]" and x:
                        x -=1
                    elif s[j] == "]" and not x:
                        break
                    j+=1
                    
                numToMulti = 0
                y = i
                
                # Find numToMulti
                while y!=-1:
                    try:
                        y-=1
                        numToMulti = int(s[y:i])
                    except:
                        break
                        
                s = s[:y+1] + numToMulti*s[i+1:j] + s[j+1:]
                
                # If the replacement also had a bracket that came after
                try:
                    int(s[i])
                except:
                    i-=1
                    
            i+=1
            
        return s
            
# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        """ 
        2 hashmaps for required and what you have

        2 pointers left and right

        2 vars of total chars found

        move right check if need char
            if need
                ++ total chars found
                add 1 to hashmap of char

                check if total chars met
                    if met
                        end loop
                        move to searching left
                    else 
                        R++
            else 
                R++

        moving left
            if this char in the need hashmap
                found a satisfying
                sub from hashmap and total found
                L++
                end loop
                start moving right
            else 
                L++
        """  
            
        required, have = {}, {}
        left, right = 0, 0
        totalReq, totalHave = len(t), 0
        minSize = 999999
        sL, sR = 0, 0
        
        for i in t:
            if i in required: required[i] +=1
            else: required[i] = 1
                
        for i in s:
            if i in have: continue
            else: have[i] = 0            

        while (right < len(s) or left < len(s)):
            # Have all letters
            if (totalReq == totalHave):
                # Update smallest string
                if (right - left < minSize):
                    sL, sR = left, right
                    minSize = right - left
                    
                # Moving left
                # If left is needed
                if (s[left] in required):
                    # left is requied to have size
                    if (have[s[left]] <= required[s[left]]):
                        totalHave-=1
                    have[s[left]] -=1
                left+=1
                
            # Moving right
            elif (right < len(s)):
                # Right string is required
                if (s[right] in required):
                    # It is needed to complete string
                    if (have[s[right]] < required[s[right]]):
                        totalHave+=1
                    have[s[right]] +=1
                right+=1

            else: break
             
        return s[sL:sR]
            
            

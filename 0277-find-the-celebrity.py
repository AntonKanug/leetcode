# https://leetcode.com/problems/find-the-celebrity/submissions/

# Idea:
# Check if a knows b => true remove a from celebs set
# If all n knows b and not know a => return b
# Else break => remove b from celebs

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebs = set([i for i in range(n)])
        
        while len(celebs):
            celeb = list(celebs)[0]
            celebs.remove(celeb) 

            known = True

            for pleb in range(n):
                if pleb == celeb: continue 
                    
                # Check pleb knows celeb
                # If true pleb is not a celeb => remove from celebs set
                if knows(pleb, celeb):
                    if pleb in celebs: celebs.remove(pleb)  
                # If not break and celeb is not celeb
                else: 
                    known = False
                    break
    
                # Check if celeb knows pleb
                # True => doesnt meet criteria => break
                if knows(celeb, pleb):
                    known = False
                    break
                    
            if known: return celeb
                    
        return -1

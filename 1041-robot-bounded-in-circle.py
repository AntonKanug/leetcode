# https://leetcode.com/problems/robot-bounded-in-circle/submissions/
# medium

# Idea:
# If the ending vector is not poining to north it will eventually end up at (0,0) in 1 or 3 turns

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = (0,0)
        vec = (0,1)
        
        for i in instructions:
            if i == 'G': 
                pos = (pos[0]+vec[0],pos[1]+vec[1])  
            elif i == 'L': 
                vec=(-vec[1],vec[0])
            elif i == 'R':
                vec=(vec[1],-vec[0])
                
        return pos == (0,0) or vec != (0,1)
        

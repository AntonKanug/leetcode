# https://leetcode.com/problems/asteroid-collision/submissions/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = [] # Output is a stack
        
        for i, val in enumerate(asteroids): 
            
            # If going left => crush all the left untill you cant move
            if val < 0: 
                while output and output[-1] > 0 and output[-1] < abs(val):
                    output.pop()
                    
                if not output or output[-1] < 0:
                    output.append(val)
                elif output[-1] == abs(val):
                    output.pop()
                
            # If going right always add
            else: output.append(val)

                
        return output
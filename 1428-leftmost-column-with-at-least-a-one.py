# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/submissions/
# O(n+m) - time (n*m matrix)
# O(1) - space

# Idea
# Start at top right if val == 0 go down a row
# If val == 1, set the result to the col and go down the col

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        i = 0
        j = dim[1]-1
        
        result = -1
        
        while(i<dim[0] and j>=0):
            
            val = binaryMatrix.get(i,j)
            
            if not val: i += 1
            else:
                result = j
                j-=1
                
        return result
                
                

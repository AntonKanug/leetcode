# https://leetcode.com/problems/set-matrix-zeroes/submissions/

# Improve by keeping 2 arrays of height and width
# If there is a 0 in a[i][j] height[i] = 0, width[j] = 0
# At end if 0 for row and col => mark entire row or col 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    self.setZeroesRowCol(matrix, i, j)
                    
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if not val: matrix[i][j] = 0

        
    def setZeroesRowCol(self, matrix, i, j):
        
        for x in range(len(matrix[0])):
            if matrix[i][x]: matrix[i][x] = None
                
        for y in range(len(matrix)):
            if matrix[y][j]: matrix[y][j] = None
                
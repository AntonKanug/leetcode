# https://leetcode.com/problems/sort-the-matrix-diagonally/submissions/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        # Sorting first row and diags
        # Sorting first col and diags
        
        for i,j,itr in [[1,0,len(mat[0])],[0,1,len(mat)]]:
            for z in range(itr):
                temp = []
                x, y = z*i, z*j
                
                while 0<=x<len(mat[0]) and 0<=y<len(mat):
                    temp.append(mat[y][x])
                    x+=1
                    y+=1

                temp.sort()
                
                x, y = z*i, z*j
                for idx, val in enumerate(temp):
                    mat[y+idx][x+idx] = val
                    
        return mat
        
    
# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
#         col,2-row
        
#         0,0 -> 0,2
#         0,2 -> 2,2
#         2,2 -> 2,0
#         2,0 -> 0,0

        
#         0,1 -> 1,2
#         1,2 -> 2,1
#         2,1 -> 1,0
#         1,0 -> 0,1

        num = 0
        leng = len(matrix[0])-1
        
        # Going by outter shell by shell
        for j in range(len(matrix[0])//2):
            # Rotating the elements in first row without last element
            for i in range(j,leng-j):
                # Swapping corners in 90 deg
                row,col=j,i
                matrix[col][leng-row],num=matrix[row][col],matrix[col][leng-row]

                for i in range(3):
                    row,col = col,leng-row
                    matrix[col][leng-row],num = num,matrix[col][leng-row]

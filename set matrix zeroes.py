https://leetcode.com/problems/set-matrix-zeroes/


# TC:O(mn) SC:O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col=False
        is_row=False
        
        #if any row from beginning is zero
        for i in range(len(matrix[0])):
            if matrix[0][i]==0:
                is_col=True
        #if any col from beginning is zero
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                is_row=True
        #starting from (1,1) and check if matrix here has 
        #any zero too store that in their respective row and col
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0 #col
                    matrix[0][j]=0 #row
        #based on above step we set values in each row and column 
        #to zero
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][0] or not matrix[0][j]:
                    matrix[i][j]=0:
        if is_row:
            for i in range(len(matrix)):
                matrix[i][0]=0
        if is_col:
            for i in range(len(matrix)):
                matrix[0][i]=0

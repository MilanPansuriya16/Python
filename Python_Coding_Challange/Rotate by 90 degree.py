'''
https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1
'''

'''
Anti-clockwise → transpose + reverse columns
Clockwise → transpose + reverse rows
'''

#########################################################################################

class Solution:
    def rotateMatrix(self, mat):
        # code here
        
        n = len(mat)
        
        # 1. Transpose the matrix
        for i in range(0,n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
                
        # 2. Reverse each column
        for j in range(0,n):
            for i in range(n//2):
                mat[i][j],mat[n-1-i][j] = mat[n-1-i][j],mat[i][j]
                
        return mat
        	
#########################################################################################
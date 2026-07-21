'''
https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1
'''


#########################################################################################

class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        
        r = len(mat)
        c = len(mat[0])
        
        rowtrack = [0 for i in range(r)]
        coltrack = [0 for j in range(c)]
        
        for i in range(0,r):
            for j in range(0,c):
                if mat[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1
                
        for i in range(0,r):
            for j in range(0,c):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    mat[i][j] = 0
                    
        return mat
	
#########################################################################################
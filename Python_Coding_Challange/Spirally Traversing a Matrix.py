'''
https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1
'''


#########################################################################################

class Solution:
    def spirallyTraverse(self, mat):
        # code here
        
        n = len(mat)         # Number of rows
        m = len(mat[0])      # Number of columns
        
        left = 0 
        right = m - 1
        top = 0
        bottom = n - 1
        
        arr = []
        
        while left <= right and top <= bottom:
            # 1. Traverse Left --> Right
            for i in range(left,right+1):
                val = mat[top][i]
                arr.append(val)
            top += 1
        
            # 2. Traverse Top --> Bottom
            for i in range(top,bottom+1):
                val = mat[i][right]
                arr.append(val)
            right -= 1
            
            # 3. Traverse Right --> Left
            if top <= bottom:
                for i in range(right,left-1,-1):
                    val = mat[bottom][i]
                    arr.append(val)
                bottom -= 1
            
            # 4. Traverse Bottom --> Top
            if left <= right:
                for i in range(bottom,top-1,-1):
                    val = mat[i][left]
                    arr.append(val)
                left += 1
                
        return arr
	
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/diameter-of-binary-tree/
'''

#########################################################################################

''' Structure of binary tree Node 
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def diameter(self, root):
        # code here
        self.diameter = 0
        def solve(node):
            if node is None:
                return 0
            
            left_height = solve(node.left)
            right_height = solve(node.right)
            
            self.diameter = max(self.diameter,left_height+right_height)
            return 1+max(left_height,right_height)
            
        solve(root)    
        return self.diameter
	
#########################################################################################
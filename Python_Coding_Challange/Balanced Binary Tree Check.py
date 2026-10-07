'''
https://www.geeksforgeeks.org/problems/check-for-balanced-tree/1
'''

#########################################################################################

''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
        # code here
        
        def solve(node):
            if node is None:
                return 0
                
            left_height = solve(node.left)
            
            if left_height == -1:
                return -1
                
            right_height = solve(node.right)
            
            if right_height == -1:
                return -1
                
            if abs(left_height - right_height) > 1:
                return -1
                
            return 1+max(left_height,right_height)
            
        x = solve(root)
        if x == -1:
            return False
        else:
            return True
	
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/height-of-binary-tree/1
'''

#########################################################################################

''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        # code here
        def solve(node):
            if node is None:
                return 0
            
            left_height = solve(node.left)
            right_height = solve(node.right)
            
            return 1 + max(left_height,right_height)
            
        return solve(root)-1
	
#########################################################################################
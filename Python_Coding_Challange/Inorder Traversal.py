'''
https://www.geeksforgeeks.org/problems/inorder-traversal/1
'''

#########################################################################################

''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self, root):
        # code here
        result = []
        
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            result.append(node.data)
            dfs(node.right)
        
        dfs(root)
        return result
	
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/postorder-traversal/1
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
    def postOrder(self, root):
        # code here
        result = []
        
        def dfs(node):
            
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            result.append(node.data)
            
        dfs(root)
        return result
        
	
#########################################################################################
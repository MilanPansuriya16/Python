'''
https://www.geeksforgeeks.org/problems/preorder-traversal/1
'''

#########################################################################################

'''Structure of Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
        result = []
        
        def dfs(node):
            if node is None:
                return
            result.append(node.data)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        return result
	
#########################################################################################
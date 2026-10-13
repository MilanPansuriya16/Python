'''
https://www.geeksforgeeks.org/problems/right-view-of-binary-tree/1
'''

#########################################################################################
from collections import deque

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def rightView(self, root):
        # code here
        result = []
        queue = deque([])
        queue.append(root)
        
        if root is None:
            return []
            
        while len(queue) != 0:
            level_size = len(queue)
            for i in range(level_size):
                e = queue.popleft()
                if i == level_size-1:
                    result.append(e.data)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
                    
        return result 
	
#########################################################################################


#########################################################################################
############################ Optimized Approach ############################
class Solution:
    def rightView(self, root):
        # code here
        ans = []
        
        def reverse_post_order(node,level):
            if node is None:
                return []
            if len(ans) == level:
                ans.append(node.data)
            if node.right:
                reverse_post_order(node.right,level+1)
            if node.left:
                reverse_post_order(node.left,level+1)
                
        reverse_post_order(root,0)
        
                    
        return ans
#########################################################################################
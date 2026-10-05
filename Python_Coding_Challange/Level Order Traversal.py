'''
https://www.geeksforgeeks.org/problems/level-order-traversal/1
'''

#########################################################################################

''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque


class Solution:
    def levelOrder(self, root):
        # code here
        result = []
        queue = deque([])
        
        def lot(node):
            queue.append(node)
            while len(queue) != 0:
                e = queue.popleft()
                result.append(e.data)
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
                
        lot(root)
        
        return result
	
#########################################################################################
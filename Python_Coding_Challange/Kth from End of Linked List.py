'''
https://www.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
'''


#########################################################################################

""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        # code here
        
        slow = head
        fast = head
        
        # Move fast k-1 steps ahead
        for i in range(k-1):
            if fast is None:
                return -1
            fast = fast.next
            
        if fast is None:
            return -1
        
        # Move both pointers until fast reaches last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        return slow.data
	
#########################################################################################
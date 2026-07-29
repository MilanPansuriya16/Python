'''
https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1
'''


#########################################################################################

""" Structure of Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        temp = head
        prev = None
        
        
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        
        return prev
	
#########################################################################################
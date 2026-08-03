'''
https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
'''


#########################################################################################

""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        
        temp = head
        
        prev = temp.prev
        
        while temp is not None:
            front = temp.next
            temp.next = prev
            temp.prev = front
            prev = temp
            temp = front
         
        head = prev   
        return head
	
#########################################################################################
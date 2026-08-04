'''
https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1
'''


#########################################################################################

"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
class Solution:
    
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        
        if head.next is None and head.data == x:
            return None
        
        temp = head
        prev = None
        new_head = head
        
        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                if temp.next:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next
            
            prev = temp
            temp = temp.next
        
        return new_head
	
#########################################################################################

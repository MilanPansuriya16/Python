'''
https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1
'''

#########################################################################################

# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, headRef):
        # code here
       curr = headRef.next
       new_head = headRef
       
       while curr:
           if curr.data == curr.prev.data:
               if curr.prev == new_head:
                   curr.prev = None
                   new_head = curr
               else:
                   curr.prev.prev.next = curr
                   curr.prev = curr.prev.prev
           curr = curr.next
         
       return new_head
    
#########################################################################################
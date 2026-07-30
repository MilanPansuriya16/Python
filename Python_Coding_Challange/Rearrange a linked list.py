'''
https://www.geeksforgeeks.org/problems/rearrange-a-linked-list/1
'''


#########################################################################################

""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def rearrangeEvenOdd(self, head):
        # code here
        
        my_list = []
        temp = head
        
        while temp and temp.next:
            val = temp.data
            my_list.append(val)
            temp = temp.next.next
        if temp:
            val = temp.data
            my_list.append(val)
            
        temp = head.next
        while temp and temp.next:
            val = temp.data
            my_list.append(val)
            temp = temp.next.next
        if temp:
            val = temp.data
            my_list.append(val)
            
        temp = head
        index = 0
        while temp is not None:
            temp.data = my_list[index]
            index += 1
            temp = temp.next

        return head
	
#########################################################################################

#--Optimized Approach--#

""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def rearrangeEvenOdd(self, head):
        # code here
        
        if head is None or head.next is None:
            return head
            
        odd = head 
        even = head.next
        even_head = even
        
        while even is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            
        odd.next = even_head
        
        return head
    
#########################################################################################

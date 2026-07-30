'''
https://www.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1
'''


#########################################################################################

""" Structure of a Linked List Node
class Node:
    def __init__(self):
        self.data = None
        self.next = None   
"""

class Solution:
    def divide(self, head):
        # code here
            
        temp = head
        even_list = []
        odd_list = []
        
        while temp:
            val = temp.data
            if val%2 == 0:
                even_list.append(val)
            else:
                odd_list.append(val)
            temp = temp.next
            
        temp = head
        for i in range(len(even_list)):
            temp.data = even_list[i]
            temp = temp.next
            
        for i in range(len(odd_list)):
            temp.data = odd_list[i]
            temp = temp.next
        
        return head
	
#########################################################################################

#--Optimized Approach--#

    
#########################################################################################

'''
https://www.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1
'''


#########################################################################################

"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        #code here
        temp = head
        my_set = set()
        
        while temp is not None:
            if temp in my_set:
                return temp.data
            else:
                my_set.add(temp)
            temp = temp.next
            
        return -1
	
#########################################################################################

#--Optimized Approach--#

"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        #code here
        
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
                
        return -1
    
#########################################################################################

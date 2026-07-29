'''
https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1
'''


#########################################################################################

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        
        temp = head
        my_set = set()
        
        while temp is not None:
            if temp in my_set:
                return True
            else:
                my_set.add(temp)
            temp = temp.next
            
        return False
	
#########################################################################################

#--Optimized Approach--#

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        
        return False
    
#########################################################################################

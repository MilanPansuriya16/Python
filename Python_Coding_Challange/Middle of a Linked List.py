'''
https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
'''


#########################################################################################

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        
        count = (count // 2)
        temp = head
        for i in range(0,count):
            temp = temp.next
        
        return temp.data
	
#########################################################################################

#--Optimized Approach--#

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
#########################################################################################
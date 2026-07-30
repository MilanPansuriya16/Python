'''
https://www.geeksforgeeks.org/problems/find-length-of-loop/1
'''


#########################################################################################

''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        
        temp = head
        travers = {}
        
        count = 0
        
        while temp is not None:
            if temp in travers:
                i = count - travers[temp]
                return i
            else:
                travers[temp] = count
            count += 1
            temp = temp.next
        
        return 0
	
#########################################################################################

#--Optimized Approach--#

''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0
    
#########################################################################################

'''
https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1
'''

#########################################################################################

# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        
        temp = head
        end = head
        result = []
        
        while end.next:
            end = end.next
            
        while temp.data < end.data:
            total = temp.data + end.data
            if total == target:
                result.append([temp.data,end.data])
                temp = temp.next
                end = end.prev
            elif total < target:
                temp = temp.next
            else:
                end = end.prev
        
        return result
    
#########################################################################################
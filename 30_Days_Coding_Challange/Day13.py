# One odd Occuring
# Array End Insert

'''
https://www.geeksforgeeks.org/problems/find-the-odd-occurence4820/1
https://www.geeksforgeeks.org/problems/array-insert-at-end/1
'''


#########################################################################################
class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        
        occur = {}
        
        for i in range(len(arr)):
            if arr[i] in occur:
                occur[arr[i]] += 1
            else:
                occur[arr[i]] = 1
        
        for key,value in occur.items():
            if value%2 == 0:
                continue
            else:
                return key
        return -1
    
#########################################################################################
class Solution:
    def insertAtEnd(self, arr, val):
       # code here
       arr.append(val)
       return arr
    
#########################################################################################
# Second Largest
# Swap the array elements
'''
https://www.geeksforgeeks.org/problems/second-largest3735/1
https://www.geeksforgeeks.org/problems/need-some-change/1
'''

#########################################################################################
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        for i in range(len(arr)):
            max_index = i 
            
            for j in range(i+1,len(arr)):
                if arr[max_index] > arr[j]:
                    continue
                else:
                    max_index = j
            
            arr[max_index],arr[i] = arr[i],arr[max_index]
            
            if i>0:
                if arr[0] > arr[i]:
                    return arr[i]
                
        return -1
    
#########################################################################################
class Solution:
    def swapElements(self, arr):
        #Code here
        
        for i in range(len(arr)):
            if i+2 <= len(arr)-1:
                arr[i],arr[i+2] = arr[i+2],arr[i]
        return arr
    
#########################################################################################
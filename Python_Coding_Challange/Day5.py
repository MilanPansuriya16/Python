# Check if array is sorted
# Remove Duplicates Sorted Array
'''
https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1
'''


#########################################################################################
class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        
        return True

#########################################################################################
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        
        j = 0
        for i in range(1,len(arr)):
            if arr[i] != arr[j]:
                j +=1
                arr[j] = arr[i]
        
        return arr[:j+1]
    
#########################################################################################
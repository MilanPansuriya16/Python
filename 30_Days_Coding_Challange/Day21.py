# Missing in Array
# Binary Search
'''
https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1
'''


#########################################################################################
class Solution:
    def missingNum(self, arr):
        # code here
        
        arr_sum = 0 
        for val in arr:
            arr_sum = arr_sum + val
        
        n = len(arr) + 1
        sum = (n*(n+1))//2
        
        return sum - arr_sum
    
#########################################################################################
class Solution:
    def binarySearch(self, arr, k):
        # code here
        start = 0
        end = len(arr)
        middle_index = len(arr)//2
        
        if k == arr[middle_index]:
            return True
        elif k < arr[middle_index]:
            end = middle_index 
        else:
            start = middle_index + 1
            
        for i in range(start,end):
            if arr[i] == k:
                return True
            
        return False
    
#########################################################################################
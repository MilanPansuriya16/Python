# Count the Zeros
# First and Last in Sorted
'''
https://www.geeksforgeeks.org/problems/count-the-zeros2550/1
https://www.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
'''


########################################################################################
class Solution:
    def countZeroes(self, arr):
        # code here
        
        start = 0
        end = len(arr)-1
        z_index = -1
        
        while(start<=end):
            mid = (start+end)//2
            if arr[mid] == 1:
                start = mid+1
            else:
                z_index = mid
                end -= 1
                
        if z_index != -1:
            return len(arr)-z_index
        else:
            return -1
        
########################################################################################
class Solution:
    def find(self, arr, x):
        # code here
        
        start = 0
        end = len(arr)-1
        first_index = -1
        
        
        while(start<=end):
            mid = (start+end)//2
            if arr[mid] == x:
                first_index = mid
                end = mid-1
            elif arr[mid] < x:
                start = mid+1
            else:
                end = mid -1
        
        start = 0
        end = len(arr)-1
        last_index = -1
        
        while(start<=end):
            mid = (start+end)//2
            if arr[mid] == x:
                last_index = mid
                start = mid+1
            elif arr[mid] < x:
                start = mid+1
            else:
                end = mid -1
        
        return [first_index,last_index]
    
########################################################################################
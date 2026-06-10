# First Occurrence in Sorted
'''
https://www.geeksforgeeks.org/problems/binary-search-1587115620/1
https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1
'''


#########################################################################################
class Solution:
    def firstSearch(self, arr, k):
        # Code Here
        
        i = 0
        j = len(arr)-1
        find_index = float('inf')
        
        while(i<=j):
            mid = (i+j)//2
            if arr[mid] == k:
                find_index = min(find_index,mid)
                j = mid-1
            elif arr[mid] < k:
                i = mid+1
            else:
                j = mid-1
                
        if find_index == float('inf'):
            return -1
        else:
            return find_index
        
#########################################################################################
class Solution:
    def findEquilibrium(self, arr):
        # code here

        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            right_sum = total_sum - left_sum - arr[i]
            if left_sum == right_sum:
                return i
            left_sum += arr[i]
        
        return -1
    
#########################################################################################
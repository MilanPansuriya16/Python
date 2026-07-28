'''
https://www.geeksforgeeks.org/problems/two-sum-in-sorted-array/1
'''

#########################################################################################

class Solution:
    def twoSum(self, arr, target):
        #code here
        
        seen_index = {}
        
        for i in range(len(arr)):
            sum = target - arr[i]
            if sum in seen_index:
                return [seen_index[sum]+1 , i+1]
            else:
                seen_index[arr[i]] = i
        
        return [-1,-1]
    
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
'''


#########################################################################################

class Solution:
    def subarraySum(self, arr, target):
        # code here
        
        l = 0
        r = 0
        sum = 0
        
        for r in range(len(arr)):
            sum += arr[r]
            
            while sum > target and l <= r:
                sum -= arr[l]
                l += 1
                
            if sum == target:
                return [l+1,r+1]
                
        return [-1]
        
#########################################################################################
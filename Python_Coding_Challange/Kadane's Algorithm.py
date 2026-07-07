'''
https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
'''

#########################################################################################

class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        maxi = float('-inf')
        total = 0
        
        for i in range(0,len(arr)):
            total += arr[i]
            maxi = max(maxi,total)
            if total < 0:
                total = 0
        return maxi
            
#########################################################################################
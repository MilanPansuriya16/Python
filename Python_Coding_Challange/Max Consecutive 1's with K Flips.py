'''
https://www.geeksforgeeks.org/problems/maximize-number-of-1s0905/1
'''

# Subarray/Substring = contiguous
# Subsequence = can skip elements
#########################################################################################
##########################  Sliding Window Approach  ##########################

class Solution:
    def maxOnes(self, arr, k):
        # code here
        
        l = 0
        r = 0
        n = len(arr)
        zero_count = 0
        maxi = 0
        
        while r < n:
            if arr[r] == 0:
                zero_count += 1
                
            if zero_count > k:
                if arr[l] == 0:
                    zero_count -= 1
                l += 1
                
            if zero_count <= k:
                maxi = max(maxi,r-l+1)
            r += 1
        return maxi
	
#########################################################################################
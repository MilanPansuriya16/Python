'''
https://www.geeksforgeeks.org/problems/find-first-repeated-character4108/1
'''

# Subarray/Substring = contiguous
# Subsequence = can skip elements
#########################################################################################

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        
        l = 0
        r = 0
        n = len(s)
        maxi = 0
        my_dict = {}
        
        while r < n:
            if s[r] in my_dict:
                pos = my_dict[s[r]]
                l = max(l,my_dict[s[r]]+1)
                    
            maxi = max(maxi,(r-l+1))
            my_dict[s[r]] = r
            r = r+1
        
        return maxi
	
#########################################################################################
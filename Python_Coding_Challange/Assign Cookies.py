'''
https://www.geeksforgeeks.org/problems/assign-cookies/1
'''

#########################################################################################

class Solution:
    def maxChildren(self, greed, cookie):
        #code here
        greed.sort()
        cookie.sort()
        i = 0
        j = 0
        count = 0
        
        
        while i < len(greed) and j < len(cookie):
            if greed[i] <= cookie[j]:
                count += 1
                i = i + 1
            j = j + 1
        
        return count
	
#########################################################################################
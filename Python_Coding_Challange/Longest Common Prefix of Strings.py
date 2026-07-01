'''
https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1
'''


#########################################################################################

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        
        if len(arr) == 0:
            return ''
        
        
        base = arr[0]
        lcp = ''

        for i in range(len(base)):
            for word in arr[1:]:
                if base[i] != word[i] or i == len(word):
                    return lcp
                
            lcp += base[i]
        return lcp
            
#########################################################################################              

'''
https://www.geeksforgeeks.org/problems/find-first-repeated-character4108/1
'''


#########################################################################################

class Solution:
    def firstRepChar(self, s):
        # code here
        
        # Boolean array for 26 lowercase letters
        seen = [False] * 26
        
        for i in s:
            index = ord(i) - ord('a')   # map 'a'->0, 'b'->1, ...
            if seen[index] == True:
                return i                # first repeat found
            seen[index] = True
            
        return -1   # if no repeated character
	
#########################################################################################
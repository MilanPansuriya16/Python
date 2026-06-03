# Reverse a String
'''
https://www.geeksforgeeks.org/problems/reverse-a-string/1
'''

#########################################################################################
class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        result = ''
        start = len(s)-1
        end = -1
        step = -1
        
        for x in range(start,end,step):
            result = result + s[x]
        
        return result
     
#########################################################################################
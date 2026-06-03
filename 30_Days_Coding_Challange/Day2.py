# Day 2: String Manipulation
'''
https://www.geeksforgeeks.org/problems/replace-all-0s-with-5/1
https://www.geeksforgeeks.org/problems/change-the-string3541/1
https://www.geeksforgeeks.org/problems/c-strings4609/1
'''

#########################################################################################
class Solution:
    def convertFive(self, n):
        # Code here
        str_n = str(n)
        result = ''
        for i in str_n:
            if i == '0':
                result = result + '5'
            else:
                result = result + i
        return result
    
#########################################################################################
class Solution:
    def modify(self, s):
        # code here
        result = ''
        first_char = s[0]
        if first_char == first_char.lower():
            result = s.lower()
        else:
            result = s.upper()
        return result
    
#########################################################################################
class Solution:
    def conCat(self,s1,s2):
        # code here
        result = s1+s2
        return result
    
#########################################################################################

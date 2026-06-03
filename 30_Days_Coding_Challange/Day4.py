# Find the camel case and count the type of characters in a string
'''
https://www.geeksforgeeks.org/problems/count-type-of-characters3635/1
https://www.geeksforgeeks.org/problems/find-the-camel3348/1
'''

'''
A - Z = 65 - 90
a - z = 97 - 122
0 - 9 = 48 - 57
'''

#########################################################################################
class Solution:
    def count (self,s):
        # your code here
        upper_case = 0 
        lower_case = 0
        numeric = 0
        special = 0
        
        for char in s:
            if ord(char) >= 65 and ord(char) <= 90:
                upper_case += 1
            elif ord(char) >= 97 and ord(char) <= 122:
                lower_case += 1
            elif ord(char) >= 48 and ord(char) <= 57:
                numeric += 1
            else:
                special += 1
        return upper_case,lower_case,numeric,special
    
#########################################################################################
class Solution:
    def countCamelCase (self,s):
        # your code here
        camel_case = 0
        for char in s:
            if ord(char) >= 65 and ord(char) <= 90:
                camel_case += 1
        return camel_case
    
#########################################################################################
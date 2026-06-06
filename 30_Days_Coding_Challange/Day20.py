# Binary Substrings with Corners as 1
# Lower case to upper case
'''
https://www.geeksforgeeks.org/problems/binary-string-1587115620/1
https://www.geeksforgeeks.org/problems/lower-case-to-upper-case3410/1
'''


#########################################################################################
class Solution:
    def binarySubstring(self, s):
        #code here
        
        count = 0
        for char in s:
            if char == '1':
                count += 1
        
        return (count * (count -1))//2
    
#########################################################################################
class Solution:
    def to_upper(self, str):
        # code here
        return str.upper()
    
#########################################################################################
# Strings Rotations of Each Other
# Remove character
'''
https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1
https://www.geeksforgeeks.org/problems/remove-character3815/1
'''


#########################################################################################
class Solution:
    def areRotations(self, s1, s2):
        # code here
        
        # new_str = ''
        # for i in range(len(s1)):
        #     if s1[i] == s2[0]:
        #         new_str = s1[i:] + s1[:i]
            
        #     if new_str == s2:
        #         return True
        # return False
        
        new_str = s1+s1
        if s2 in new_str:
            return True 
        else:
            return False
        
#########################################################################################
class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        
        result = ''
        for char in str1:
            if char not in str2:
                result += char
            else:
                continue
        
        return result
    
#########################################################################################
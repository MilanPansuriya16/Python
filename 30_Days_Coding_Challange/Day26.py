# Replace Consecutive Two Same with One
# Alternate Merge two strings
'''
https://www.geeksforgeeks.org/problems/consecutive-elements2306/1
https://www.geeksforgeeks.org/problems/merge-two-strings2736/1
'''


##############################################################################
class Solution:
    def removeDuplicates(self, s):
        # code here
        
        result = ''
        
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                continue
            else:
                result = result + s[i]
        
        result = result + s[len(s)-1]
        
        return result
    
##############################################################################
class Solution:
    def merge(self, s1, s2):
        # code here
        
        a = len(s1)
        b = len(s2)
        result = ''
        
        if a <= b:
            for i in range(a):
                    result = result + s1[i] + s2[i]
            result = result + s2[len(s1):len(s2)]
        else:
            for i in range(b):
                    result = result + s1[i] + s2[i]
            result = result + s1[len(s2):len(s1)]
                    
        return result
    
##############################################################################
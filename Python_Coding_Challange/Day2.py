# Union of Arrays with Duplicates
# Palindrome String
'''
https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1
https://www.geeksforgeeks.org/problems/palindrome-string0817/1
'''


#########################################################################################
class Solution:    
    def findUnion(self, a, b):
        # code here
        a1 = set(a)
        b1 = set(b)
        result = a1.union(b1)
        
        return sorted(result)
    
#########################################################################################
class Solution:
    def isPalindrome(self, s):
        # code here
        
        rev_str = ''
        for char in range(len(s)-1,-1,-1):
            rev_str += s[char]
        
        if rev_str == s:
            return True
        else:
            return False
        
#########################################################################################
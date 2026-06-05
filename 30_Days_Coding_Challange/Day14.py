# Check for Subsequence
# Remove Common and Concat
'''
https://www.geeksforgeeks.org/problems/given-two-strings-find-if-first-string-is-a-subsequence-of-second/1
https://www.geeksforgeeks.org/problems/remove-common-characters-and-concatenate-1587115621/1
'''


#########################################################################################
class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        
        start = 0
        count = 0
        
        for char in s1:
            if start <= len(s2):
                for i in range(start,len(s2)):
                    if char == s2[i]:
                        count += 1
                        start = i       
                        break
        
        if count == len(s1):
            return True
        else:
            return False
        
#########################################################################################
class Solution:
    def concatenatedString(self,s1,s2):
        #code here
        
        output = ''
        
        for char in s1:
            if char in s2:
                continue
            else:
                output = output + char
        
        for char in s2:
            if char in s1:
                continue
            else:
                output = output + char
            
        if len(output) == 0:
            return -1
        else:
            return output
        
#########################################################################################

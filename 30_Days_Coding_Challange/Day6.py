# Check if a string is Isogram or not
'''
https://www.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not-1587115620/1
https://www.geeksforgeeks.org/problems/java-delete-alternate-characters4036/1
'''

#########################################################################################
class Solution:
    def isIsogram(self,s):
        #Your code here
        dict1 = {}
        for char in s:
            if char in dict1:
                return False
            else:
                dict1[char] = 1
        return True
  
#########################################################################################
class Solution:
    def delAlternate (self, s):
        # code here 
        output = ''
        for i in range(0,len(s),2):
            output = output + s[i]
        return output
    
#########################################################################################


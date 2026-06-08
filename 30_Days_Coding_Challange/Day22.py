# Panagram Checking
# Uncommon characters
# Most Frequent Character
'''
https://www.geeksforgeeks.org/problems/pangram-checking-1587115620/1
https://www.geeksforgeeks.org/problems/uncommon-characters4932/1
https://www.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1
'''


##########################################################################################
class Solution:
    def checkPangram(self,s):
        #code here
        
        a = [0] * 26
        s = s.lower()
        
        for i in range(len(s)):
            if s[i].isalpha():
                a[ord(s[i])-97] += 1
            
        for i in range(len(a)):
            if a[i] == 0:
                return False
                
        return True
    
##########################################################################################
class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        #code here
        result = set(s1) ^ set(s2)
        result = sorted(result)
        result = ''.join(result)
        
        return result
    
##########################################################################################
class Solution:
    def getMaxOccurringChar(self, s):
        #code here
        
        # dict = {}
        
        # for char in s:
        #     if char in dict:
        #         dict[char] += 1
        #     else:
        #         dict[char] = 1
        
        # max = 0
        
        # for key,value in dict.items():
        #     if max < value:
        #         max = value
        
        # list = []
        # for key,value in dict.items():
        #     if value == max:
        #         list.append(key)
                
        # list = sorted(list)    
        
        # return list[0]
        
        
        list = [0] * 26
        
        for i in range(len(s)):
            list[ord(s[i])-97] += 1
            
        
        max_frq = max(list)
        
        for i in range(26):
            if max_frq == list[i]:
                return chr(i+97)
            
##########################################################################################
# Repeated Character and Non Repeating Character
'''
https://www.geeksforgeeks.org/problems/repeated-character2058/1
https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/1
'''

#########################################################################################
class Solution:
    def firstRep(self, s):
        # code here
        dict1 = {}
        
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for key,value in dict1.items():
            if value > 1:
                return key
            
        return '#'
    
#########################################################################################
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        dict1 = {}
    
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for key,value in dict1.items():
            if value == 1:
                return key
        
        return '$'
    
#########################################################################################
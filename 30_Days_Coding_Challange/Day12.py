# Python3 program to convert a list of characters into a string
# Capitalize First Letter of Words
'''
https://www.geeksforgeeks.org/problems/upper-case-conversion5419/1
https://www.geeksforgeeks.org/problems/convert-a-list-of-characters-into-a-string5142/1
'''


#########################################################################################
class Solution:
    def convert(self, s: str) -> str:
        # code here
        new_s = s.split(' ')
        for i in range(len(new_s)):
            char = new_s[i]
            if char:
                word = char[0].upper()
                new_word = word + char[1:]
                new_s[i] = new_word
        
        output = ' '.join(new_s)
        return output
    
#########################################################################################
class Solution:
    def chartostr(self, arr,N):
        # code here
        output = ''
        for char in arr:
            output = output + str(char)
            
        return output
    
#########################################################################################
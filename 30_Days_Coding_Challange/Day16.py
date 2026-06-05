# First Occurence
# First Letter of Every Word
'''
https://www.geeksforgeeks.org/problems/implement-strstr/1
https://www.geeksforgeeks.org/problems/print-first-letter-of-every-word-in-the-string3632/1
'''


#########################################################################################
class Solution:
    def firstOccurence(self,txt,pat):
        #code here
        
        for i in range(len(txt)):
            val = pat[0]
            if txt[i] == val:
                if pat == txt[i:i+len(pat)] and i+len(pat) <= len(txt):
                    return i
        return -1
    
#########################################################################################
class Solution:
    def firstAlphabet(self, s):
        # code here
        list = s.split(' ')
        result = ''
        for char in list:
            result = result + char[0]
        return result
     
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1
'''


#########################################################################################

class Solution:
    def removeDuplicates(self, s):
        # code here
        
        dict = {}
        
        for i in s:
            if i in dict:
                continue
            else:
                dict[i] = 1
        
        result = ''
        
        for key,value in dict.items():
            result += key
            
        return result
	
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/find-the-odd-occurence4820/1
'''


#########################################################################################

class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        
        result = 0
        
        for num in arr:
            result = result ^ num
        
        return result
	
#########################################################################################
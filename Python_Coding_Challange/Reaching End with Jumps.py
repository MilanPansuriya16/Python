'''
https://www.geeksforgeeks.org/problems/jump-game/1
'''

#########################################################################################

class Solution:
    def canReach(self, arr):
        # code here
        max_index = 0
        
        for i in range(len(arr)):
            if i > max_index:
                return False
            max_index = max(max_index,i+arr[i])
             
        return True
	
#########################################################################################
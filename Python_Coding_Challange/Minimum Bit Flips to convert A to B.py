'''
https://www.geeksforgeeks.org/problems/bit-difference-1587115620/1
'''


#########################################################################################

class Solution:
    def countBitsFlip(self, a, b):
        #code here
        
        ans = a ^ b
        count = 0
        
        for i in range(0,32):
            if ans & (1<<i) != 0:
                count += 1
        
        return count
	
#########################################################################################
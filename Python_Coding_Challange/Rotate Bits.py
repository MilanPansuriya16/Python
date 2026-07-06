'''
https://www.geeksforgeeks.org/problems/rotate-bits4524/1
'''


#########################################################################################

class Solution:
    def rotate(self, n, d):
        # Number of bits
        BITS = 16

        # If D > 16
        d = d % BITS

        # Left Rotation
        left = ((n << d) | (n >> (BITS - d))) & 0xFFFF

        # Right Rotation
        right = ((n >> d) | (n << (BITS - d))) & 0xFFFF

        return [left, right]
	
#########################################################################################
'''
https://leetcode.com/problems/reverse-integer/
'''

#########################################################################################

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = str(x)
        n = len(rev)
        if x < 0:
            rev = rev[0] + rev[n:0:-1]
        else:
            rev = rev[::-1]

        ans = int(rev)

        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        
        return ans
    
#########################################################################################
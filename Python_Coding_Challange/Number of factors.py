'''
https://www.geeksforgeeks.org/problems/number-of-factors1435/1
'''

#########################################################################################

class Solution:
    def countFactors (self, n):
        # code here
        # square root of n
        a = n ** 0.5
        a = int(a)
        count = 0
        
        for i in range(1,a+1):
            if n % i == 0:
                # If factors are equal (e.g., 6*6 = 36), count it once
                if i * i == n:
                    count += 1
                else:
                    # Count both i and n // i
                    count += 2
                    
        return count
	
#########################################################################################
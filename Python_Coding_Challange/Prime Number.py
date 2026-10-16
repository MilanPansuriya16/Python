'''
https://www.geeksforgeeks.org/problems/prime-number2314/1
'''

#########################################################################################

class Solution:
    def isPrime(self, n):
        # code here
        
        # Numbers less than or equal to 1 are not prime
        if n <= 1:
            return False
        
        # 2 is the only even prime number
        if n == 2:
            return True
        
        # Exclude all other even numbers
        if n % 2 == 0:
            return False
            
        # Check odd factors up to the square root of n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
            
        return True
    
#########################################################################################
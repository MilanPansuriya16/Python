'''
https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1
'''

# Greedy Approach #
#########################################################################################

class Solution:
    def findMin(self, n: int) -> int:
       # code here 
       arr = [10,5,2,1]
       min_coin = 0
       
       
       for coin in arr:
           if n == 0:
               return min_coin
           if n//coin > 0:
               temp = n//coin
               min_coin += temp
               n -= temp * coin
               
       return min_coin
            
######################################################################################### 
# Day 3 of 30 Days Coding Challenge
# Sum of Array Elements
'''
https://www.geeksforgeeks.org/problems/reverse-coding2452/1
https://www.geeksforgeeks.org/problems/sum-all-array-elements/1
'''


#########################################################################################
class Solution:
    def sumOfNaturals(self, n):
        # code here 
        result = 0
        if n == 0:
            return 0
        else: 
            for i in range(n+1):
                result = result + i
        return result
    
#########################################################################################
class Solution:
    def arraySum(self, arr):
        # code here
        result = 0
        for i in arr:
            result = result + i
        return result
    
#########################################################################################
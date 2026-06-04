# Palindrome Array
'''
https://www.geeksforgeeks.org/problems/perfect-arrays4645/1
https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
'''

#########################################################################################
import copy
class Solution:
    def isPalindrome(self, arr):
        # code here
        rvs_arr = copy.deepcopy(arr)
        i = 0
        j = len(rvs_arr)-1
        while(i < j):
            rvs_arr[i],rvs_arr[j] = rvs_arr[j],rvs_arr[i]
            i += 1
            j -= 1
        if arr == rvs_arr:
            return True
        else:
            return False
        
#########################################################################################
class Solution:
    def search(self, arr, x):
        # code here
        for i in range(len(arr)):
            if x == arr[i]:
                return i
            
        return -1        

#########################################################################################
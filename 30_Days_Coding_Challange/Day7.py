# Day 7: Prime Number and Swap Kth Elements
'''
https://www.geeksforgeeks.org/problems/prime-number2314/1
https://www.geeksforgeeks.org/problems/swap-kth-elements5500/1
'''


#########################################################################################
class Solution:
    def isPrime(self, n):
        # code here
        start = 2
        end = (n//2) + 1
        if n == 1:
            return False
        else:
            for num in range(start,end):
                if n%num == 0:
                    return False
        return True
    
#########################################################################################
 class Solution:
    def swapKth(self, arr, k):
        # Code Here
        beg_index = k-1
        end_index = k
        
        arr[beg_index],arr[-end_index] = arr[-end_index],arr[beg_index]
    
        return arr
       
#########################################################################################
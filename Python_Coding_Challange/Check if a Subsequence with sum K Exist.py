'''
https://www.geeksforgeeks.org/problems/check-if-there-exists-a-subsequence-with-sum-k/1
'''


#########################################################################################

class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        
        def backtrack(index,total):
            if total == k:
                return True
            elif total > k:
                return False
            if index >= len(arr):
                return False
            
            new_sum = total + arr[index]
            pick = backtrack(index + 1, new_sum)
            if pick == True:
                return True
            
            new_sum = total
            not_pick = backtrack(index + 1, new_sum)
            
            return not_pick
            
        return backtrack(0,0)
            
#########################################################################################              

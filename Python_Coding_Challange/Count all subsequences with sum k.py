
#########################################################################################

class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        
        def backtrack(index,total):
            if total == k:
                return 1
            elif total > k:
                return 0
            if index >= len(arr):
                return 0
            
            new_sum = total + arr[index]
            pick = backtrack(index + 1, new_sum)

            new_sum = total
            not_pick = backtrack(index + 1, new_sum)
            
            return pick + not_pick
            
        return backtrack(0,0) 
            
######################################################################################### 
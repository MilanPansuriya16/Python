# Backtracking & Recursion #
#########################################################################################

class Solution:
    def checkSubsequenceSum(self, arr, k):
        # code here
        
        result = []
        
        def backtrack(index,total,subset):
            if total == k:
                result.append(subset.copy())
                return 
            elif total > k:
                return
            if index >= len(arr):
                return 
        
            subset.append(arr[index])
            new_sum = total + arr[index]
            backtrack(index+1,new_sum,subset)
            e = subset.pop()
            new_sum -= e
            backtrack(index+1,new_sum,subset)
            
        backtrack(0,0,[])
        
        return result

#########################################################################################
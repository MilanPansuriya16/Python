'''
https://www.geeksforgeeks.org/problems/combination-sum-iii--111703/1
'''

# Backtracking & Recursion #
#########################################################################################

class Solution:
    
    def combinationSum(self, n, k):
        # code here
        result = []
        
        def solve(last,total,subset):
            if total == n and len(subset) == k:
                result.append(subset.copy())
                return 
        
            if total > n or len(subset) > k:
                return
            
            for i in range(last,10):
                new_total = total + i
                subset.append(i)
                solve(i+1, new_total,subset)
                subset.pop()
            
        solve(1,0,[])
                
        return result
            
######################################################################################### 
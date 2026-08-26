'''
https://www.geeksforgeeks.org/problems/combination-sum-1587115620/1
'''

# Backtracking & Recursion #
#########################################################################################

class Solution:
    
    def solve(self,index,total,subset,nums,target,result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return
        if index >= len(nums):
            return
        
        new_total = total + nums[index]
        subset.append(nums[index])
        self.solve(index,new_total,subset,nums,target,result)
        
        new_total = total
        subset.pop()
        self.solve(index + 1,new_total,subset,nums,target,result)
        
    def targetSumComb(self, arr: list[int], target: int) -> list[list[int]]:
        # code here
        result = []
        self.solve(0,0,[],arr,target,result)
        
        return result
            
#########################################################################################              

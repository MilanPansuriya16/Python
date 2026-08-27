'''
https://www.geeksforgeeks.org/problems/combination-sum-ii-1664263832/1
'''

# Backtracking & Recursion #
#########################################################################################

class Solution:

    def solve(self,index,total,subset,nums,result):
        if total == 0:
            result.append(subset.copy())
            return
        if total < 0:
            return
        if index >= len(nums):
            return
        
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            new_total = total - nums[i]
            self.solve(i+1,new_total,subset,nums,result)
            subset.pop()

    
    def uniqueCombinations(self, arr: list[int], target: int) -> list[list[int]]:
        # code here
        arr.sort()
        result = []
        self.solve(0,target,[],arr,result)
    
        return result
            
#########################################################################################              

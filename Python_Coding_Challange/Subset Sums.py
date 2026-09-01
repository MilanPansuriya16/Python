'''
https://www.geeksforgeeks.org/problems/subset-sums2234/1
'''

# Backtracking & Recursion #
#########################################################################################

class Solution:
    
    def solve(self,index,arr,total,result):
        if index >= len(arr):
            result.append(total)
            return
        
        # Include current element
        self.solve(index+1,arr,total + arr[index],result)
        
        # Exclude current element
        self.solve(index+1,arr,total,result)
        
    def subsetSums(self, arr):
        # code here
        result = []
        total = 0
        
        self.solve(0,arr,total,result)
        
        return result
            
#########################################################################################              

'''
https://www.geeksforgeeks.org/problems/generate-all-binary-strings/1
'''

# Backtracking & Recursion #
#########################################################################################

class Solution:
    
    def backtrack(self,index,numbers,result):
        if index >= len(numbers):
            result.append("".join(numbers))
            return
        
        numbers[index] = "0"
        self.backtrack(index+1,numbers,result)
        
        numbers[index] = "1"
        self.backtrack(index+1,numbers,result)
        
        
    def binstr(self, n):
        # code here
        result = []
        numbers = ["0"]*n
        
        self.backtrack(0,numbers,result)
        
        return result
            
#########################################################################################              

'''
https://www.geeksforgeeks.org/problems/generate-all-possible-parentheses/1
'''

# Backtracking & Recursion #
#########################################################################################

class Solution:
    
    def backtrack(self,index,total,brackets,result):
        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        if total > len(brackets)//2 or total < 0:
            return
        
        
        brackets[index] = "("
        new_total = total + 1
        self.backtrack(index+1,new_total,brackets,result)
        
        new_total = total - 1
        brackets[index] = ")"
        self.backtrack(index+1,new_total,brackets,result)
        
        
        
    def generateParentheses(self, n: int) -> list[str]:
        #code here
        result = []
        brackets = [""] * n
        
        self.backtrack(0,0,brackets,result)
        
        return result
            
######################################################################################### 
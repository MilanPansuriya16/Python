'''
https://www.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1
'''

# Backtracking & Recursion #
#########################################################################################

class Solution:
    def possibleWords(self, arr: list[int]) -> list[str]:
        # code here
        
        mp = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = []
        
        def solve(index,subset):
            
            
            if index >= len(arr):
                if subset:
                    result.append("".join(subset.copy()))
                return
            
            letters = mp[arr[index]]
            
            if not letters:
                solve(index+1,subset)
                return
            
            for ch in letters:
                subset.append(ch)
                solve(index+1,subset)
                subset.pop()
                
        solve(0,[])    
        return result
            
#########################################################################################              

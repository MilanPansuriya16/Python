'''
https://www.geeksforgeeks.org/problems/power-set4302/1
'''


#########################################################################################

class Solution:
    def powerSet(self, s):
        # Code here
        result = []
    
        def func(index, subset):
            if index >= len(s):
                result.append("".join(subset))
                return
    
            # Include current character
            subset.append(s[index])
            func(index + 1, subset)
    
            # Exclude current character
            subset.pop()
            func(index + 1, subset)
    
    
        func(0,[])
        result.sort()   # lexicographical order
        return result
            
#########################################################################################              

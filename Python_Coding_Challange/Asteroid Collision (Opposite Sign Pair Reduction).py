'''
https://www.geeksforgeeks.org/problems/opposite-sign-pair-reduction/1
'''


#########################################################################################
########################    Stack based solution    ########################

class Solution:
    def reducePairs(self, arr):
        # code here
        stack = []
        n = len(arr)
        
        for i in range(0,n):
            curr = arr[i]
            
            # A collision is possible only when the last stored value and the current value move in opposite directions.
            while stack and stack[-1] * curr < 0:
                if abs(stack[-1]) < abs(curr):
                    stack.pop()
                    
                # Both destroy each other, so nothing is added.
                elif abs(stack[-1]) == abs(curr):
                    stack.pop()
                    curr = None
                    break
                
                # The current value is destroyed by a larger one in the stack.
                else: # abs(stack[-1]) > abs(curr)
                    curr = None
                    break
                
            if curr is not None:
                stack.append(curr)
    
        return stack
	
#########################################################################################
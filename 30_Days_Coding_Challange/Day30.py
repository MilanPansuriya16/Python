# Parenthesis Checker
# Run Length Encoding
'''
https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1
https://www.geeksforgeeks.org/problems/run-length-encoding/1
'''

########################################################################################
class Solution:
    def isBalanced(self, s):
        # code here
        
        stack = []
        open_b = '({['
        
        for char in s:
            if char in open_b:
                stack.append(char)
            else:
                if stack:
                    pop_char = stack.pop()
                else:
                    return False
                if char == ')':
                    if pop_char == '(':
                        continue
                    else:
                        return False
                elif char == '}':
                    if pop_char == '{':
                        continue
                    else:
                        return False
                elif char == ']':
                    if pop_char == '[':
                        continue
                    else:
                        return False

        if stack:
            return False
        else:
            return True

########################################################################################       
class Solution:
    def encode(self, s : str) -> str:
        # code here
        
        result = []
        count = 1
        for i in range(len(s)-1):
            j = i
            if s[i] == s[i+1]:
                count += 1
            else:
                result.append(s[i])
                result.append(str(count))
                count = 1
       
        result.append(s[-1])
        result.append(str(count))
        output = ''.join(result)
        
        return output

########################################################################################
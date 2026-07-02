'''
https://www.geeksforgeeks.org/problems/roman-number-to-integer3201/1
'''

'''
*** Step by Step Approach ***
1) Define values for Roman symbols
-->I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.

2) Iterate through the string
-->Look at the current symbol and the next one.
-->If the current symbol is smaller than the next, subtract it.
-->Otherwise, add it.

3) Return the total.
'''

#########################################################################################

class Solution:
    def romanToDecimal(self, s): 
        # code here
        
        value = {
                    'I':1
                ,   'V':5
                ,   'X':10
                ,   'L':50
                ,   'C':100
                ,   'D':500
                ,   'M':1000
                }
        
        result = 0
        
        for i in range(len(s)):
            if i+1 < len(s) and value[s[i]] < value[s[i+1]]:
                result -= value[s[i]]
            else:
                result += value[s[i]]
                
        return result
    
#########################################################################################
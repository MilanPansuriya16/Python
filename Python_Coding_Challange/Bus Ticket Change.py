'''
https://www.geeksforgeeks.org/problems/bus-ticket-change/1
'''

# Greedy Approach #
#########################################################################################

class Solution:
    def canServe(self, arr):
        # code here 
        
        five = 0
        ten = 0
        
        for coin in arr:
            if coin == 5:
                five += 1
            elif coin == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five >= 1 and ten >= 1:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five = five -3
                else:
                    return False
        return True
            
######################################################################################### 
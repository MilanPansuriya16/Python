# Value equal to position
# Count Smaller in an Array
'''
https://www.geeksforgeeks.org/problems/value-equal-to-index-value1330/1
https://www.geeksforgeeks.org/problems/count-of-smaller-elements5947/1
'''


#########################################################################################
class Solution:
    def valEqualToPos(self, arr):
        # code here
        output = []
        
        for i,num in enumerate(arr):
            if i+1 == num:
                output.append(num)
        return output
    
#########################################################################################
class Solution:
    def countOfElements(self, x, arr):
        # code here
        count = 0
        for i in arr:
            if i <= x:
                count += 1
        return count
    
#########################################################################################

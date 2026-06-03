# Day 5: Largest Element in an Array and Search an Element in an Array
'''
https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
'''


#########################################################################################
class Solution:
    def largest(self, arr):
        # code here
        largest_ele = float('-inf')
        for i in arr:
            if i > largest_ele:
                largest_ele = i
            else:
                continue
        return largest_ele
    
#########################################################################################
class Solution:
    def search(self, arr, x):
        # code here
        find_index = -1
        if x in arr:
            for i in range(len(arr)):
                if x == arr[i]:
                    find_index = i
                    return find_index
        else:
            return find_index
        
#########################################################################################
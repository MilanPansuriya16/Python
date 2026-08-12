'''
https://www.geeksforgeeks.org/problems/subsets-1613027340/1
'''


#########################################################################################

class Solution:
    def subsets(self, arr):
        # code here
        
        n = len(arr)
        total_subset = 1<<n
        result = []
        
        for num in range(0,total_subset):
            new_list = []
            for i in range(0,n):
                if num & (1<<i) != 0:
                    new_list.append(arr[i])
                
            result.append(new_list)
        
        return result
	
#########################################################################################
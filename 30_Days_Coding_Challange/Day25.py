# Missing And Repeating
# Array Leaders
# Find element at a given Index
'''
https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
'''


#########################################################################################
class Solution:
    def findTwoElement(self, arr):
        # code here
        
        e_set = set()
        
        for val in arr:
            if val in e_set:
                repeat = val
                break
            else:
                e_set.add(val)
        
        arr_sum = sum(arr) 
        
        # for val in arr:
        #     arr_sum += val
            
        n = len(arr)
        total_sum = (n*(n+1))//2
        
        miss_val = total_sum-(arr_sum-repeat)
        return [repeat,miss_val]
    
#########################################################################################
    def leaders(self, arr):
        # code here
    
        max_leader = arr[len(arr)-1]
        list_1 = []
        list_1.append(max_leader)
        
        start = len(arr)-2
        end = -1
        for i in range(start,end,-1):
            if arr[i] >= max_leader:
                max_leader = arr[i]
                list_1.append(max_leader)
                
        return list_1[::-1]
    
#########################################################################################

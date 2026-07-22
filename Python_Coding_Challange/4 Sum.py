'''
https://www.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1
'''


#########################################################################################

class Solution:
    def fourSum(self, arr, target):
        # code here
        
        n = len(arr)
        result = set()
        
        for i in range(0,n):
            for j in range(i+1,n):
                hash_set = set()
                for k in range(j+1,n):
                    forth = target - (arr[i]+arr[j]+arr[k])
                    if forth in hash_set:
                        new_ele = [arr[i],arr[j],arr[k],forth]
                        new_ele.sort()
                        result.add(tuple(new_ele))
                    hash_set.add(arr[k])
        
        result = list(result)
        result.sort()
        return result

#########################################################################################
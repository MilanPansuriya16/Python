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
#--Optimized Approach--#

class Solution:
    def fourSum(self, arr, target):
        # code here
        
        n = len(arr)
        arr.sort()
        result = []
        
        for i in range(0,n):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            
            for j in range(i+1,n):
                if j > i+1 and arr[j] == arr[j-1]:
                    continue
                
                k = j + 1
                l = n - 1
                
                while k < l:
                    total = arr[i] + arr[j] + arr[k] + arr[l]
                    if total == target:
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        result.append(temp)
                        k += 1
                        l -= 1
                        
                        while k < l and arr[k] == arr[k-1]:
                            k += 1
                        while l > k and arr[l] == arr[l+1]:
                            l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
        return result
    
#########################################################################################
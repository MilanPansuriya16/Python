'''
https://www.geeksforgeeks.org/problems/three-sum/1
'''


#########################################################################################

class Solution:
    def triplets(self, arr ):
        # code here
        
        result = set()
        
        n = len(arr)
        for i in range(0,n):
            my_set = set()
            for j in range(i+1,n):
                third = 0 - (arr[i] + arr[j])
                if third in my_set:
                    temp = [arr[i],arr[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(arr[j])
                
        result = list(result)
        result.sort()
        return result
	
#########################################################################################
#--Optimized Approach--#

class Solution:
    def triplets(self, arr ):
        # code here
        
        n = len(arr)
        result = []
        
        arr.sort()
        
        for i in range(0,n):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            
            j = i+1
            k = n-1
            
            while j < k:
                total_sum = arr[i] + arr[j] + arr[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    temp = [arr[i] , arr[j] , arr[k]]
                    result.append(temp)
                    j += 1
                    k -= 1
                    
                    while j < k and arr[j] == arr[j-1]:
                        j += 1
                    while j < k and arr[k] == arr[k+1]:
                        k -= 1
        return result  
    
#########################################################################################
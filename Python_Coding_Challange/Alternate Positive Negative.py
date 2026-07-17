'''
https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1
'''


#########################################################################################

class Solution:
    def rearrange(self,arr):
        # code here
        
        n_freq = []
        p_freq = []
        for i in range(0,len(arr)):
            if arr[i] < 0:
                n_freq.append(arr[i])
            else:
                p_freq.append(arr[i])
        

        n = len(p_freq)
        m = len(n_freq)
        i = 0 
        j = 0
        k = 0
        
        while i < n and j < m:
            arr[k] = p_freq[i]
            arr[k+1] = n_freq[j]
            i += 1
            j += 1
            k += 2
            
        while i < n:
            arr[k] = p_freq[i]
            i += 1
            k += 1
            
        while j < m:
            arr[k] = n_freq[j]
            j += 1
            k += 1
            
            
        return arr
	
#########################################################################################
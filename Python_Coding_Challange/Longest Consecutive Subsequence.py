'''
https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1
'''


#########################################################################################

class Solution:
    def longestConsecutive(self, arr):
        # code here
        
        n = len(arr)
        my_set = set()
        
        for i in range(0,n):
            my_set.add(arr[i])
            
        
        longest = 0
        
        for num in my_set:
            if num-1 not in my_set:
                v = num
                count = 1
                while v+1 in my_set:
                    count += 1
                    v += 1
                longest = max(longest,count)
        
        return longest
	
#########################################################################################
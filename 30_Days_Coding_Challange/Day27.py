# Minimum distance in an Array
# Two Sum - Pair with Given Sum
'''
https://www.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1
https://www.geeksforgeeks.org/problems/key-pair5616/1
'''


#########################################################################################
class Solution:
    def minDist(self, arr, x, y):
        
        x_index = -1
        y_index = -1
        min_dist = float('inf')
        
        for i in range(len(arr)):
            if arr[i] == x:
                x_index = i
                
            if arr[i] == y:
                y_index = i
            
            if x_index != -1 and y_index != -1:
                min_dist = min(min_dist,abs(x_index - y_index))
                
        if min_dist != float('inf'):
            return min_dist
        else:
            return -1
        
#########################################################################################
class Solution:
	def twoSum(self, arr, target):
		# code here
		
		if len(arr) < 2:
			return False
			
		arr = sorted(arr)
		i = 0
		j = len(arr) - 1
		
		while i < j:
			total = arr[i] + arr[j]
			if total == target:
				return True
			elif total < target:
				i += 1
			else:
				j -= 1
		return False

#########################################################################################

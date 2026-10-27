'''
https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
'''


#########################################################################################
########################    Array    ########################

class Solution:
	def pushZerosToEnd(self, arr: list[int]) -> None:
		# code here
		n = len(arr)
		curr = 0

		for i in range(n):
			if arr[i] != 0:
				arr[i], arr[curr] = arr[curr], arr[i]
				curr += 1

		return arr
	
#########################################################################################
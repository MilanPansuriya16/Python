# Move All Zeroes to End
# Reverse Words
'''
https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
'''

#########################################################################################
class Solution:
	def pushZerosToEnd(self, arr):
		# code here
		current = 0
		for i in range(len(arr)):
			if arr[i] != 0:
				arr[current], arr[i] = arr[i], arr[current]
				current += 1
		return arr

#########################################################################################
class Solution:
    def reverseWords(self, s):
        # code here
        
        new_list = s.split('.')
        
        new_list.reverse()
        
        result = '.'.join(new_list[i] for i in range(len(new_list)) if new_list[i] != '')
       
        return result
	
#########################################################################################
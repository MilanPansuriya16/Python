# Day 1: Print Alternate Elements of an Array and Count Odd Even
'''
https://www.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1?page=1&category=Arrays&difficulty=Basic&sortBy=submissions
https://www.geeksforgeeks.org/problems/count-odd-even/1
'''

#########################################################################################
class Solution:
	def countOddEven(self, arr):
		#Code here
		odd_element = 0 
		even_element = 0
		for num in arr:
		    if num%2 == 0:
		        even_element = even_element + 1
		    else:
		        odd_element = odd_element + 1
		return odd_element,even_element 
	
#########################################################################################
class Solution:
    def getAlternates(self, arr):
        # Code Here
        alternate_element = []
        for i in range(len(arr)):
            if i%2 == 0:
                alternate_element.append(arr[i])
        return alternate_element

#########################################################################################
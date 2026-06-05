# 1 to n Without Loops
# Alternates in an Array
'''
https://www.geeksforgeeks.org/problems/print-1-to-n-without-using-loops3621/1
https://www.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1
'''


#########################################################################################
class Solution:
	def printTillN(self, n):
		#code here 
		if n == 0:
			return
		self.printTillN(n-1)
		print(n, end = ' ')
		
#########################################################################################
class Solution:
    def getAlternates(self, arr):
        # Code Here
        alternate = []
        for i in range(len(arr)):
            if i % 2 == 0:
                alternate.append(arr[i])
        return alternate
    
#########################################################################################

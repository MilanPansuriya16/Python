# Remove Vowels from String
# Remove Spaces
'''
https://www.geeksforgeeks.org/problems/remove-vowels-from-string1446/1
https://www.geeksforgeeks.org/problems/remove-spaces0128/1
'''

#########################################################################################
class Solution:
	def removeVowels(self, s):
		# code here
		vowel = ['a','e','i','o','u']
		result = ''
		for i in s:
			if i.lower() in vowel:
				continue
			else:
				result = result + i
		return result
	
#########################################################################################
class Solution:
    def removeSpaces(self, s):
        # code here
        new_list = s.split(' ')
        new_string = ''.join(new_list)
        return new_string
	
#########################################################################################
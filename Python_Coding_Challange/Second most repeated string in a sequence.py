'''
https://www.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence0534/1
'''


#########################################################################################

class Solution:
    def secFrequent(self, arr):
        # code here
        # Handle empty array
        if not arr:
            return -1
            
        # Build frequency dictionary manually
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
                
        # If only one unique string    
        if len(freq)==1:
            return -1
            
        # Extract frequencies
        freq_values = list(freq.values())
        
        # highest frequency
        max_index = -1
        for value in freq_values:
            if max_index < value:
                max_index = value
        
        # second highest frequency
        sec_max_index = -1
        for value in freq_values:
            if sec_max_index < value and value < max_index:
                sec_max_index = value
                
        return sec_max_index
        	
#########################################################################################
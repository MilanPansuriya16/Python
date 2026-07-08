'''
https://www.geeksforgeeks.org/problems/maximum-number-of-characters-between-any-two-same-character4552/1
'''

'''
*** Step by Step Approach ***
1) Track first occurrence of each character
-->Use a dictionary to store the index of the first time each character appears.

2) Calculate distance for repeats
-->When you encounter the same character again, compute the distance between the current index and the first index.
-->The number of characters between them is (current_index - first_index - 1).
-->Otherwise, add it.

3) Update maximum
-->Keep track of the maximum distance found so far.

4) Edge cases
-->If no character repeats → return -1.
'''

#########################################################################################

class Solution:

    def maxCharGap(self, s: str) -> int:
        # code here
        
        first_index = {}
        max_distance = -1
        
        for i, ch in enumerate(s):
            if ch not in first_index:
                first_index[ch] = i
            else:
                # characters between = current_index - first_index - 1
                distance = i - first_index[ch] - 1
                max_distance = max(max_distance, distance)
        
        return max_distance
    
#########################################################################################
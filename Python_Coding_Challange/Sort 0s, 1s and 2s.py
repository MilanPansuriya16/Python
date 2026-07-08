'''
https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
'''

'''
*** Step by Step Approach ***
1) Maintain 3 variables low, high and mid
-->low - all elements before low are 0
-->mid - all elements between low and mid are 1
-->high - all elements after high are 2

2) Initially low, mid are set at 0 and high is at n-1

3) Now, we iterate mid from 0 to high, and for every element
-->if it is equal to 0, we swap it with element at low, and increement low and mid
-->else if it is equal to 2, we swap it with element at high, and decreement high
-->else we just increement mid (i.e element is equla to 1)
'''

#########################################################################################

class Solution:
    def sort012(self, arr):
        # code here
        
        low = 0
        mid = 0
        high = len(arr) - 1
        
        while(mid<=high):
            if arr[mid] == 0:
                arr[low],arr[mid] = arr[mid],arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 2:
                arr[mid],arr[high] = arr[high],arr[mid]
                high -= 1
            else:
                mid += 1
        
        return arr
    
#########################################################################################
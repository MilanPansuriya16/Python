'''
https://www.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1
'''

'''
*** Step by Step Approach ***

1) Initialize Binary Search Pointers
--> Set low = 0 and high = n - 1.
--> The minimum element will always lie within this range.

2) Find the Middle Element
--> Calculate mid = (low + high) // 2.
--> Compare arr[mid] with arr[high] to determine which half contains the minimum.

3) Check Which Half is Unsorted
--> If arr[mid] > arr--> The minimum lies in the right half.
    --> Move low = mid + 1.

--> Otherwise:
    --> The minimum is either at mid or in the left half.
    --> Move high = mid.

4) Reduce the Search Space
--> Repeat the above steps until low becomes equal to high.
--> Each iteration eliminates half of the remaining elements.

5) Return the Minimum Element
--> When low == high, that position points to the minimum element.
--> Return arr[low].

6) Edge Case
--> If the array is not rotated, the first element itself is the minimum.
--> The above logic still correctly returns it.
'''

#########################################################################################

class Solution:
    def findMin(self, arr):
        # code here
        
        i = 0
        j = len(arr) - 1
        minm = float('inf')
        
        while i <= j:
            mid = (i + j)//2
            
            
            if arr[mid] <= arr[j]:
                minm = min(minm,arr[mid])
                j = mid - 1
            else:
                minm = min(minm,arr[i])
                i = mid + 1
                
        return minm
            
#########################################################################################
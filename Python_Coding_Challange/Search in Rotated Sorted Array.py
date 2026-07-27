'''
https://www.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1
'''


'''
*** Step by Step Approach ***

1) Initialize Two Pointers
--> Set i = 0 and j = n - 1.

2) Find Middle Element
--> Calculate mid = (i + j) // 2.
--> If arr[mid] == key, return mid.

3) Check Sorted Half
--> At least one half of the rotated array is always sorted.
--> If arr[mid] <= arr[j], the right half is sorted.
--> Otherwise, the left half is sorted.

4) Verify Target Range
--> If the target lies within the sorted half,
    search in that half.
--> Otherwise, search in the other half.

5) Update Search Space
--> Move i or j accordingly to discard half of the array.
--> This reduces the search space in every iteration.

6) Repeat
--> Continue until i > j or the target is found.

7) Target Not Found
--> If the loop ends without finding the key,
    return -1.

'''

#########################################################################################

class Solution:
    def search(self, arr, key):
        # code here

        i = 0
        j = len(arr)-1
        
        while i <= j:
            mid = (i + j) // 2
            
            if arr[mid] == key:
                return mid
                
            if arr[mid] <= arr[j]:
                if arr[mid] <= key <= arr[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if arr[i] <= key <= arr[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
        return -1
            
#########################################################################################
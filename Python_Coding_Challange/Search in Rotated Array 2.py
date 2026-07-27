'''
https://www.geeksforgeeks.org/problems/search-in-rotated-array-2/1
'''

'''
*** Step by Step Approach ***

1) Initialize Binary Search
--> Set two pointers:
    i = 0 (start)
    j = n - 1 (end)

2) Find Middle Element
--> Calculate:
    mid = (i + j) // 2
--> If arr[mid] == key, return True.

3) Handle Duplicates
--> If arr[i] == arr[mid] == arr[j],
    we cannot determine the sorted half.
--> Shrink the search space:
    i += 1
    j -= 1

4) Identify the Sorted Half
--> If arr[mid] <= arr[j],
    the right half is sorted.
--> Otherwise,
    the left half is sorted.

5) Check Target in Right Half
--> If the right half is sorted and:
    arr[mid] <= key <= arr[j]
    search in the right half:
    i = mid + 1
--> Otherwise:
    j = mid - 1

6) Check Target in Left Half
--> If the left half is sorted and:
    arr[i] <= key <= arr[mid]
    search in the left half:
    j = mid - 1
--> Otherwise:
    i = mid + 1

7) Repeat the Process
--> Continue until i > j or the key is found.

8) Key Not Found
--> If the loop ends without finding the key,
    return False.

'''

#########################################################################################

class Solution:
    def search(self, arr, key):
        # code here
        
        i = 0 
        j = len(arr) - 1
        
        while i <= j:
            mid = (i + j)//2
            
            if arr[mid] == key:
                return True
            
            if arr[mid] == arr[i] == arr[j]:
                i += 1
                j -= 1
                continue
            
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
        return False
            
#########################################################################################
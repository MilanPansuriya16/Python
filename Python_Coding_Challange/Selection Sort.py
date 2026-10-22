'''
https://www.geeksforgeeks.org/problems/selection-sort/1
'''

#########################################################################################
##########################  Selection Sort  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given an unsorted array, sort it in ascending order using the Selection Sort algorithm.
Goal: Return the array sorted in-place from smallest to largest.

APPROACH - SELECTION SORT (In-place Comparison):
-------------------------------------------------
Key Insight: Divide the array into a sorted left portion and an unsorted right portion.
In each pass, find the minimum element from the unsorted portion and swap it into
its correct position at the boundary — growing the sorted portion by one each time.

Strategy:
- Outer loop marks the current boundary (position i) between sorted and unsorted
- Inner loop scans from i+1 to end to find the index of the minimum element
- Swap arr[i] with arr[min_index] to place the smallest unsorted element correctly
- Repeat until the entire array is sorted

ALGORITHM STEPS:
----------------
1. n = length of arr
2. For i from 0 to n-1 (outer loop — current sorted boundary):
   a. Set min_index = i (assume current position holds the minimum)
   b. For j from i+1 to n-1 (inner loop — scan unsorted portion):
      - If arr[j] < arr[min_index], update min_index = j
   c. Swap arr[i] and arr[min_index]
3. Return arr (sorted in-place)

EXAMPLE WALKTHROUGH:
--------------------
Input: arr = [64, 25, 12, 22, 11]

Pass i=0: min in [64,25,12,22,11] → index 4 (val 11) → swap → [11, 25, 12, 22, 64]
Pass i=1: min in [25,12,22,64]    → index 2 (val 12) → swap → [11, 12, 25, 22, 64]
Pass i=2: min in [25,22,64]       → index 3 (val 22) → swap → [11, 12, 22, 25, 64]
Pass i=3: min in [25,64]          → index 3 (val 25) → swap → [11, 12, 22, 25, 64]
Pass i=4: single element, no change

Answer: [11, 12, 22, 25, 64]

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n²)
- Two nested loops: outer runs n times, inner runs n-i-1 times → total ~n²/2 comparisons
- Always O(n²) regardless of input order (no early exit)

Space Complexity: O(1)
- Sorting is done in-place with only a constant number of extra variables
'''

#########################################################################################

class Solution: 
    def selectionSort(self, arr):
        # code here
        n = len(arr)
        
        for i in range(n):
            min_index = i
            
            for j in range(i+1,n):
                if arr[min_index] > arr[j]:
                    min_index = j
                
            arr[i],arr[min_index] = arr[min_index],arr[i]
        
        return arr
            
#########################################################################################              

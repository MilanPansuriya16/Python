'''
https://www.geeksforgeeks.org/problems/bubble-sort/1
'''

#########################################################################################
##########################  Bubble Sort (Optimized with Early Exit)  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given an unsorted array, sort it in ascending order using the Bubble Sort algorithm.
Goal: Return the array sorted in-place from smallest to largest.

APPROACH - BUBBLE SORT WITH EARLY EXIT:
----------------------------------------
Key Insight: In each pass, the largest unsorted element "bubbles up" to its correct
position at the end. After k passes, the last k elements are guaranteed sorted.
Optimization: If a full pass completes with no swaps, the array is already sorted
— break early instead of continuing unnecessary passes.

Strategy:
- Outer loop controls the number of passes (at most n passes needed)
- Inner loop compares adjacent pairs and swaps if out of order
- Shrink the inner loop by i each pass (last i elements are already sorted)
- Track swapped flag; if no swap happened in a pass, exit early

ALGORITHM STEPS:
----------------
1. n = length of arr
2. For i from 0 to n-1 (outer loop — pass number):
   a. Set swapped = False
   b. For j from 0 to n-i-2 (inner loop — compare adjacent pairs):
      - If arr[j] > arr[j+1]: swap them, set swapped = True
   c. If swapped == False: break (array is already sorted)
3. Return arr

EXAMPLE WALKTHROUGH:
--------------------
Input: arr = [64, 34, 25, 12, 22]

Pass i=0: [64,34]→swap [34,64,25,12,22] | [64,25]→swap [34,25,64,12,22] | [64,12]→swap [34,25,12,64,22] | [64,22]→swap → [34,25,12,22,64]  swapped=True
Pass i=1: [34,25]→swap [25,34,12,22,64] | [34,12]→swap [25,12,34,22,64] | [34,22]→swap → [25,12,22,34,64]  swapped=True
Pass i=2: [25,12]→swap [12,25,22,34,64] | [25,22]→swap → [12,22,25,34,64]  swapped=True
Pass i=3: [12,22]→no swap | [22,25]→no swap → swapped=False → break early

Answer: [12, 22, 25, 34, 64]

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n²) worst/average case, O(n) best case
- Worst: already reverse-sorted → n² comparisons
- Best: already sorted → single pass with no swaps, exits immediately via early exit

Space Complexity: O(1)
- Sorting is done in-place; only the swapped flag uses extra space
'''

#########################################################################################

class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        
        for i in range(n):
            swapped = False
            
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    swapped = True
                
                
            if swapped == False:
                break
        
        return arr
	
#########################################################################################
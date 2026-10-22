'''
https://www.geeksforgeeks.org/problems/insertion-sort/1
'''

#########################################################################################
##########################  Insertion Sort (Shift & Insert)  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given an unsorted array, sort it in ascending order using the Insertion Sort algorithm.
Goal: Return the array sorted in-place from smallest to largest.

APPROACH - INSERTION SORT (Shift & Insert):
--------------------------------------------
Key Insight: Think of it like sorting playing cards in hand — pick one card at a time
and insert it into its correct position among the already-sorted cards to its left.
The left portion [0..i-1] is always sorted; we insert arr[i] into that sorted portion.

Strategy:
- Start from index 1 (single element at index 0 is trivially sorted)
- Pick the current element as key
- Shift all sorted elements greater than key one position to the right
- Drop key into the gap created — its correct sorted position

ALGORITHM STEPS:
----------------
1. n = length of arr
2. For i from 1 to n-1 (outer loop — pick each unsorted element):
   a. key = arr[i]  (element to be inserted)
   b. j = i - 1     (start comparing from the last sorted element)
   c. While j >= 0 and arr[j] > key:
      - Shift: arr[j+1] = arr[j]
      - Move left: j -= 1
   d. Place key: arr[j+1] = key
3. Return arr

EXAMPLE WALKTHROUGH:
--------------------
Input: arr = [12, 11, 13, 5, 6]

i=1, key=11: j=0, arr[0]=12 > 11 → shift → [12,12,13,5,6]; j=-1 → place → [11,12,13,5,6]
i=2, key=13: j=1, arr[1]=12 < 13 → stop → place at j+1=2 → [11,12,13,5,6]  (no change)
i=3, key=5:  j=2, arr[2]=13>5 → shift; j=1, arr[1]=12>5 → shift; j=0, arr[0]=11>5 → shift
             j=-1 → place at 0 → [5,11,12,13,6]
i=4, key=6:  j=3, arr[3]=13>6 → shift; j=2, arr[2]=12>6 → shift; j=1, arr[1]=11>6 → shift
             j=0, arr[0]=5 < 6 → stop → place at j+1=1 → [5,6,11,12,13]

Answer: [5, 6, 11, 12, 13]

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n²) worst/average case, O(n) best case
- Worst: reverse-sorted input → every element shifts all the way left → n²/2 shifts
- Best: already sorted → inner while never executes → single pass O(n)

Space Complexity: O(1)
- Sorting is done in-place; only key and j use extra space
'''

#########################################################################################

class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key
            
        return arr
	
#########################################################################################
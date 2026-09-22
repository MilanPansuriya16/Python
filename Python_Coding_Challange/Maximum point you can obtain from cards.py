'''
https://www.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/1
'''

# Subarray/Substring = contiguous
# Subsequence = can skip elements
#########################################################################################
##########################  Sliding Window Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given an array of integers cardPoints and an integer k, you need to pick exactly k cards.
You can only pick cards from either the beginning or the end of the array.
Goal: Maximize the sum of points of the k cards you pick.

APPROACH - SLIDING WINDOW:
---------------------------
Key Insight: Since we can only pick from the ends (left or right), we have limited combinations:
- Pick all k from left (0 from right)
- Pick k-1 from left, 1 from right
- Pick k-2 from left, 2 from right
- ...
- Pick 0 from left, all k from right

Total combinations = k + 1

Strategy:
1. Start with picking all k cards from the left side (initial window)
2. Then gradually slide the window: remove one card from left, add one card from right
3. Track the maximum sum across all combinations

ALGORITHM STEPS:
----------------
1. Calculate sum of first k cards (all from left side) - this is our initial window
2. Set this sum as the maximum
3. Use two pointers:
   - left pointer: starts at k-1 (rightmost card in left selection)
   - right pointer: starts at n-1 (rightmost card in array)
4. Slide the window k times:
   - Remove card at left pointer from sum
   - Add card at right pointer to sum
   - Update maximum if current sum is greater
   - Move both pointers left (shrink left selection, expand right selection)
5. Return the maximum sum

EXAMPLE WALKTHROUGH:
--------------------
cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3

Initial: Pick first 3 from left
Sum = 1 + 2 + 3 = 6, max = 6

Iteration 1: Remove 3 (left), Add 1 (right)
Sum = 1 + 2 + 1 = 4, max = 6

Iteration 2: Remove 2 (left), Add 6 (right)
Sum = 1 + 6 + 1 = 8, max = 8

Iteration 3: Remove 1 (left), Add 5 (right)
Sum = 5 + 6 + 1 = 12, max = 12

Answer: 12 (pick 3 cards from right: 5, 6, 1)

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(k)
- We iterate k times to calculate initial sum
- We iterate k times to slide the window
- Total: 2k = O(k)

Space Complexity: O(1)
- Only using a few variables (curr_sum, maxi, left, right, n)
- No extra data structures needed
'''

#########################################################################################

class Solution:
    def maxScore(self, cardPoints, k):
        # code here.

        curr_sum = 0
        maxi = 0
        n = len(cardPoints)

        if n == k:
            return sum(cardPoints)

        for i in range(0,k):
            curr_sum = curr_sum + cardPoints[i]
        maxi = curr_sum

        left = k-1
        right = n-1

        while left >= 0:
            curr_sum -= cardPoints[left]
            curr_sum += cardPoints[right]

            maxi = max(maxi,curr_sum)

            left -= 1
            right -= 1

        return maxi
	
#########################################################################################
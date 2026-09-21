'''
Longest Subarray with At most Two Distinct (Fruit Into Baskets)
https://www.geeksforgeeks.org/problems/longest-subarray-with-atmost-two-distinct-integers/1

Problem: Find the length of the longest contiguous subarray with at most 2 distinct elements

Example:
arr = [1, 2, 1, 2, 3]
Output: 4 (subarray [1, 2, 1, 2])

arr = [4, 4, 4, 4]
Output: 4 (entire array has only 1 distinct element)

Approach: Sliding Window with Frequency Map
Time: O(n) | Space: O(1) - at most 3 elements in dictionary
'''

# Subarray/Substring = contiguous
# Subsequence = can skip elements
#########################################################################################
##########################  Sliding Window Approach  ##########################

class Solution:
    def totalElements(self, arr):
        """
        Core Idea:
        - Maintain a sliding window [l, r] with at most 2 distinct elements
        - Expand window by moving right pointer (r)
        - Shrink window from left (l) when we exceed 2 distinct elements
        - Track maximum window size seen
        """

        # Two pointers defining window boundaries
        l = 0  # left pointer (start of window)
        r = 0  # right pointer (end of window)
        n = len(arr)

        # Dictionary to store frequency of each element in current window
        # Key: element value, Value: count of that element
        my_dict = {}

        # Stores the maximum length of valid window seen so far
        maxi = 0

        # Expand window by moving right pointer
        while r < n:
            # Step 1: Add current element to window
            # Increment frequency count for arr[r]
            my_dict[arr[r]] = my_dict.get(arr[r], 0) + 1

            # Step 2: Check if window is invalid (more than 2 distinct elements)
            # If invalid, shrink window from left
            if len(my_dict) > 2:
                # Remove leftmost element from window
                my_dict[arr[l]] -= 1

                # If frequency becomes 0, delete from dictionary
                # IMPORTANT: This ensures len(my_dict) correctly reflects distinct count
                if my_dict[arr[l]] == 0:
                    del my_dict[arr[l]]

                # Move left pointer to shrink window
                l = l + 1

            # Step 3: Window is now valid (at most 2 distinct elements)
            # Update maximum length if current window is larger
            if len(my_dict) <= 2:
                maxi = max(maxi, r - l + 1)  # Window size = r - l + 1

            # Move right pointer to next position
            r += 1

        return maxi


# Test cases for revision
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Multiple distinct elements
    arr1 = [1, 2, 1, 2, 3]
    print(f"Input: {arr1}")
    print(f"Output: {sol.totalElements(arr1)}")  # Expected: 4 → [1,2,1,2]
    print()

    # Test 2: All same elements
    arr2 = [4, 4, 4, 4]
    print(f"Input: {arr2}")
    print(f"Output: {sol.totalElements(arr2)}")  # Expected: 4 → entire array
    print()

    # Test 3: Exactly 2 distinct elements
    arr3 = [1, 2, 1, 2, 1]
    print(f"Input: {arr3}")
    print(f"Output: {sol.totalElements(arr3)}")  # Expected: 5 → entire array
    print()

    # Test 4: Optimal window in middle
    arr4 = [0, 1, 2, 2]
    print(f"Input: {arr4}")
    print(f"Output: {sol.totalElements(arr4)}")  # Expected: 3 → [1,2,2]
    print()


#########################################################################################
'''
KEY REVISION POINTS:

1. PATTERN RECOGNITION:
   - "Longest subarray with constraint" → Think SLIDING WINDOW
   - "At most K distinct" → Use frequency map + two pointers

2. WHY SLIDING WINDOW WORKS:
   - We don't need to check every possible subarray (that would be O(n²))
   - Window moves in one direction only → left never goes backward
   - Each element visited at most twice → O(n) time

3. CRITICAL STEPS (In Order):
   Step 1: Expand window → Add arr[r] to dictionary
   Step 2: Make valid → If invalid (>2 distinct), shrink from left
   Step 3: Calculate → Update max length for current valid window
   Step 4: Continue → Move r forward

4. COMMON MISTAKES TO AVOID:
   ✗ Forgetting to delete key when count becomes 0
     → len(my_dict) will be wrong
   ✗ Checking if len(my_dict) <= 2 inside the if block
     → Should be after shrinking, as separate check
   ✗ Not using get() with default 0
     → KeyError when element not in dict

5. WHY DELETE WHEN COUNT = 0?
   - We use len(my_dict) to check distinct count
   - If we keep keys with 0 count, len() will be incorrect
   - Example: dict = {1:0, 2:1, 3:1} → len=3 but only 2 elements actually present

6. WINDOW SIZE CALCULATION:
   - Window spans from index l to r (inclusive)
   - Size = r - l + 1
   - Example: l=2, r=5 → elements at [2,3,4,5] → size = 5-2+1 = 4

7. RELATED PROBLEMS (Same Pattern):
   - Longest Substring with K Distinct Characters
   - Max Consecutive Ones with K Flips
   - Longest Substring Without Repeating Characters (K=all distinct)
   - Fruit Into Baskets (K=2, this problem)

8. TIME & SPACE ANALYSIS:
   - Time: O(n) - each element processed at most twice (by r and l)
   - Space: O(1) - dictionary holds at most 3 elements (when we detect >2 and shrink)

9. DRY RUN EXAMPLE:
   arr = [1, 2, 1, 2, 3]

   r=0: dict={1:1}, len=1, maxi=1 → [1]
   r=1: dict={1:1,2:1}, len=2, maxi=2 → [1,2]
   r=2: dict={1:2,2:1}, len=2, maxi=3 → [1,2,1]
   r=3: dict={1:2,2:2}, len=2, maxi=4 → [1,2,1,2]
   r=4: dict={1:2,2:2,3:1}, len=3 (INVALID!)
        → Shrink: remove arr[0]=1, dict={1:1,2:2,3:1}, l=1
        → len=3, maxi stays 4

   Final answer: 4

10. WHEN TO USE THIS PATTERN:
    ✓ "Longest/Maximum contiguous subarray/substring"
    ✓ "At most K distinct/different elements"
    ✓ "With constraint on window validity"
    ✗ "Minimum" → Different sliding window variant
    ✗ "Subsequence" → DP problem, not sliding window
'''
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
'''

#########################################################################################
##########################  BFS / Jump Game (Greedy BFS)  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given an array where each element represents the maximum number of steps
you can jump forward from that position, find the minimum number of jumps
to reach the last index.
Goal: Return the minimum number of jumps to reach arr[n-1], or -1 if not possible.

APPROACH - GREEDY BFS (Level-by-Level):
----------------------------------------
Key Insight: Treat each "jump" as a BFS level — all positions reachable in k jumps
form one level. The farthest position reachable from the current level becomes the
boundary of the next level.

Strategy:
- Use [left, right] as the current "level" window of reachable positions
- For each level, compute the farthest index reachable from any position in that window
- Advance the window to [right+1, farthest] and increment jump count
- If farthest never moves beyond the current window, we're stuck → return -1

ALGORITHM STEPS:
----------------
1. Initialize jump=0, left=0, right=0 (starting window covers just index 0)
2. While right < n-1 (haven't reached last index yet):
   a. Compute farthest = max(i + arr[i]) for all i in [left, right]
   b. If farthest == 0 (and we're stuck at position 0), return -1
   c. Slide window: left = right+1, right = farthest
   d. Increment jump count
3. Return total jumps

EXAMPLE WALKTHROUGH:
--------------------
Input: arr = [2, 3, 1, 1, 4]

Initial: jump=0, left=0, right=0

Level 1: window=[0,0]
  i=0: farthest = max(0, 0+2) = 2
  → left=1, right=2, jump=1

Level 2: window=[1,2]
  i=1: farthest = max(0, 1+3) = 4
  i=2: farthest = max(4, 2+1) = 4
  → left=3, right=4, jump=2

right(4) == n-1(4) → exit loop
Answer: 2 jumps

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n)
- Each index is visited exactly once across all levels (left never goes back)

Space Complexity: O(1)
- Only a constant number of variables used (jump, left, right, farthest)
'''

#########################################################################################

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        # code here
        jump = 0
        left = 0
        right = 0
        n = len(arr)
        
        while right < n-1:
            farthest = 0
            for i in range(left,right+1):
                farthest = max(farthest,i+arr[i])
            left = right+1
            right = farthest
            jump += 1
            
            if farthest == 0:
                return -1
        return jump
	
#########################################################################################
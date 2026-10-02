'''
https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
'''

#########################################################################################
##########################  Two Pointer (Sorted Events)  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given arrival times (arr) and departure times (dep) for trains at a station,
find the minimum number of platforms required so no train has to wait.
Goal: Return the minimum number of platforms needed at any point in time.

APPROACH - TWO POINTER ON SORTED ARRAYS:
-----------------------------------------
Key Insight: If we sort arrivals and departures independently, we can simulate
train events in order — a new arrival increases demand, a departure frees a platform.
We only need a departure to happen before the next arrival to avoid overlap.

Strategy:
- Sort both arrays independently
- Use pointer i for arrivals, j for departures
- If next arrival comes before or at the current earliest departure → need a new platform
- Otherwise a train has left → platform is freed, advance departure pointer
- Track the running maximum of platforms in use

ALGORITHM STEPS:
----------------
1. Sort arr and dep independently
2. Initialize count=0 (current platforms in use), ans=0 (max so far)
3. Use i=0 (arrival pointer), j=0 (departure pointer)
4. While i < n:
   a. If arr[i] <= dep[j]: a train arrives before the earliest departure → count++, i++
   b. Else: a train has departed → count--, j++
   c. Update ans = max(ans, count)
5. Return ans

EXAMPLE WALKTHROUGH:
--------------------
Input: arr = [900, 940, 950, 1100, 1500, 1800]
       dep = [910, 1200, 1120, 1130, 1900, 2000]

After sorting: arr = [900,940,950,1100,1500,1800], dep = [910,1120,1130,1200,1900,2000]

i=0,j=0: arr[0]=900 <= dep[0]=910 → count=1, i=1 | ans=1
i=1,j=0: arr[1]=940 > dep[0]=910 → count=0, j=1 | ans=1
i=1,j=1: arr[1]=940 <= dep[1]=1120 → count=1, i=2 | ans=1
i=2,j=1: arr[2]=950 <= dep[1]=1120 → count=2, i=3 | ans=2
i=3,j=1: arr[3]=1100 <= dep[1]=1120 → count=3, i=4 | ans=3
i=4,j=1: arr[4]=1500 > dep[1]=1120 → count=2, j=2 | ans=3
i=4,j=2: arr[4]=1500 > dep[2]=1130 → count=1, j=3 | ans=3
i=4,j=3: arr[4]=1500 > dep[3]=1200 → count=0, j=4 | ans=3
i=4,j=4: arr[4]=1500 <= dep[4]=1900 → count=1, i=5 | ans=3
i=5,j=4: arr[5]=1800 <= dep[4]=1900 → count=2, i=6 | ans=3

Answer: 3 platforms

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n log n)
- Sorting both arrays dominates; the two-pointer scan is O(n)

Space Complexity: O(1)
- No extra data structures; sorting is in-place
'''

#########################################################################################

class Solution:
    def minPlatform(self, arr: list[int], dep: list[int]) -> int:
        # code here
        
        arr.sort()
        dep.sort()
        ans = 0
        count = 0
        
        i = 0
        j = 0
        
        while i < len(arr):
            if arr[i] <= dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            
            ans = max(ans,count)
            
        return ans
	
#########################################################################################
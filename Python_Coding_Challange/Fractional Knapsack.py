'''
https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
'''

#########################################################################################
##########################  Greedy Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given weights and values of n items, we need to put these items in a knapsack of capacity W
to get the maximum total value in the knapsack.

Unlike 0/1 Knapsack, you are allowed to break items (take fractions of items).

Input:
- val[]: array of values of items
- wt[]: array of weights of items
- capacity: maximum weight the knapsack can hold

Output: Maximum value we can obtain (rounded to 6 decimal places)

Goal: Maximize the total value in the knapsack by taking items or fractions of items

APPROACH - GREEDY:
---------------------------
Key Insight: To maximize value, we should prioritize items with the highest value-to-weight ratio.
Taking items with better ratios first will give us maximum value for the weight we use.

Strategy:
- Calculate value/weight ratio for each item
- Sort items in descending order of this ratio (greedy choice)
- Take items greedily starting from the highest ratio
- If we can take the full item, take it
- If we can only take partial item, take the fraction that fits
- Continue until knapsack is full or no items remain

Why Greedy works here:
- We want maximum value per unit weight
- Taking highest ratio items first guarantees optimal solution
- Unlike 0/1 Knapsack, we can take fractions, so greedy approach is optimal

ALGORITHM STEPS:
----------------
1. Create a 2D array where each element is [value, weight] for an item
2. Sort this array in descending order based on value/weight ratio
3. Initialize total_val = 0 and track remaining capacity
4. Iterate through sorted items:
   a. If capacity becomes 0, break (knapsack is full)
   b. If current item's weight <= remaining capacity:
      - Take the entire item
      - Add its full value to total_val
      - Reduce capacity by item's weight
   c. If current item's weight > remaining capacity:
      - Calculate fraction that fits: (value/weight) * remaining_capacity
      - Add fractional value to total_val
      - Set capacity to 0 (knapsack is now full)
5. Return the total_val rounded to 6 decimal places

'''

#########################################################################################

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        arr = []
        
        for i in range(len(val)):
            temp = [val[i],wt[i]]
            arr.append(temp)
            
        arr.sort(key = lambda x:x[0]/x[1],reverse = True)
        
        total_val = 0
        
        for val,wt in arr:
            if capacity == 0:
                break
            
            if capacity > 0:
                if wt <= capacity:
                    capacity -= wt
                    total_val += val
                else:
                    temp_val = (val/wt)*capacity
                    capacity = 0
                    total_val += temp_val
                
        return round(total_val,6)

#########################################################################################

'''
EXAMPLE WALKTHROUGH:
--------------------
Input:
val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50

Step 1: Create array with [value, weight] pairs
arr = [[60, 10], [100, 20], [120, 30]]

Step 2: Calculate ratios and sort by ratio (descending)
Item [60, 10]: ratio = 60/10 = 6.0
Item [100, 20]: ratio = 100/20 = 5.0
Item [120, 30]: ratio = 120/30 = 4.0

Sorted arr = [[60, 10], [100, 20], [120, 30]]

Step 3: Greedy selection
capacity = 50, total_val = 0

Iteration 1: [60, 10] (ratio=6.0)
- capacity > 0, weight=10 <= capacity=50
- Take full item: total_val = 0 + 60 = 60
- capacity = 50 - 10 = 40

Iteration 2: [100, 20] (ratio=5.0)
- capacity > 0, weight=20 <= capacity=40
- Take full item: total_val = 60 + 100 = 160
- capacity = 40 - 20 = 20

Iteration 3: [120, 30] (ratio=4.0)
- capacity > 0, weight=30 > capacity=20
- Take fraction: temp_val = (120/30) * 20 = 4 * 20 = 80
- total_val = 160 + 80 = 240
- capacity = 0

Answer: 240.000000 (maximum value obtainable)

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n log n)
- Creating the array takes O(n)
- Sorting the items takes O(n log n)
- Iterating through items takes O(n)
- Overall: O(n log n) due to sorting

Space Complexity: O(n)
- We create an array to store [value, weight] pairs: O(n)
- Sorting might use O(log n) auxiliary space
- Overall: O(n)
''''
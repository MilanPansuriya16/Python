'''
https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
'''

#########################################################################################
##########################  Digit Power Sum  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given a number n, determine whether it is an Armstrong number (also called a narcissistic number).
A number with k digits is an Armstrong number if the sum of each digit raised to the power k equals n.
Example: 153 → 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓
Goal: Return True if n is an Armstrong number, False otherwise.

APPROACH - DIGIT POWER SUM:
----------------------------
Key Insight: Convert n to a string to easily extract individual digits and count them.
The power k is simply the number of digits. Sum each digit^k and compare to original n.

Strategy:
- Convert n to string to get digits and length in one step
- Use length as the exponent (power)
- Accumulate the sum of each digit raised to power
- Compare the total to the original number

ALGORITHM STEPS:
----------------
1. Convert n to string → num; compute power = len(num)
2. Initialize total = 0
3. For each character i in num:
   a. total += int(i) ** power
4. Return True if total == n, else False

EXAMPLE WALKTHROUGH:
--------------------
Input: n = 153

num = "153", power = 3

Iteration:
  i='1' → total = 0 + 1³ = 1
  i='5' → total = 1 + 5³ = 1 + 125 = 126
  i='3' → total = 126 + 3³ = 126 + 27 = 153

total(153) == n(153) → True

Counter-example: n = 123
  1³ + 2³ + 3³ = 1 + 8 + 27 = 36 ≠ 123 → False

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(k)
- k = number of digits in n; we iterate over each digit exactly once

Space Complexity: O(k)
- O(k) to store the string representation of n
'''

#########################################################################################

class Solution:
    def armstrongNumber (self, n):
        # code here 
        
        num = str(n)
        total = 0
        power = len(num) 
        
        for i in num:
            total += int(i)**power
        
        if total == n:
            return True
        else:
            return False
    
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/count-digits-in-given-number-n-which-divide-n3331/1
'''

#########################################################################################
##########################  Divisibility Rules (Digit-by-Digit Check)  Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
Given a number N as a string s, count how many of its digits divide N evenly.
A digit d divides N if N % d == 0 (digits equal to 0 are skipped as division by 0 is undefined).
Goal: Return the count of digits in N that divide N.

APPROACH - PRECOMPUTED DIVISIBILITY RULES:
-------------------------------------------
Key Insight: Instead of computing N % d directly (N can be astronomically large as a string),
use classic divisibility rules for digits 1–9 which only require:
  - digit_sum  : sum of all digits (for rules of 3, 6, 9)
  - last       : last digit        (for rules of 2, 5, 6)
  - last2      : last 2 digits     (for rule of 4)
  - last3      : last 3 digits     (for rule of 8)
  - rem7       : N mod 7 computed via rolling modulo (for rule of 7)

Strategy:
- Precompute these five values once before iterating over digits
- For each digit d in the number, apply the corresponding divisibility rule
- Skip d == 0 to avoid division by zero
- Increment count whenever the rule confirms divisibility

Divisibility Rules Used:
  1 → always divides
  2 → last digit is even
  3 → digit_sum % 3 == 0
  4 → last 2 digits % 4 == 0
  5 → last digit is 0 or 5
  6 → divisible by both 2 and 3
  7 → rolling modulo: iterate digits left-to-right, rem = (rem*10 + d) % 7
  8 → last 3 digits % 8 == 0
  9 → digit_sum % 9 == 0

ALGORITHM STEPS:
----------------
1. Compute digit_sum = sum of all digits in s
2. Compute last = int(s[-1]), last2 = int(s[-2:]), last3 = int(s[-3:])
3. Compute rem7 by iterating s: rem7 = (rem7 * 10 + d) % 7
4. For each character ch in s:
   a. d = int(ch); skip if d == 0
   b. Apply the rule for d from the table above
   c. If rule holds, count += 1
5. Return count

EXAMPLE WALKTHROUGH:
--------------------
Input: s = "1248"  (N = 1248)

Precompute:
  digit_sum = 1+2+4+8 = 15
  last      = 8
  last2     = 48
  last3     = 248
  rem7: (0*10+1)%7=1 → (1*10+2)%7=5 → (5*10+4)%7=5 → (5*10+8)%7=6  → rem7=6

Check each digit:
  d=1 → always divides → count=1
  d=2 → last(8) % 2 == 0 ✓ → count=2
  d=4 → last2(48) % 4 == 0 ✓ → count=3
  d=8 → last3(248) % 8 == 0 ✓ → count=4

Answer: 4

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(n)
- n = number of digits; each digit is visited a constant number of times

Space Complexity: O(1)
- Only a fixed set of precomputed variables; no extra data structures
'''

#########################################################################################

class Solution:    
    def divisibleByDigits(self,s):
        #code here
        n = len(s)
        digit_sum = sum(int(ch) for ch in s)
        
        last = int(s[-1])
        last2 = int(s[-2:]) if n >= 2 else last
        last3 = int(s[-3:]) if n >= 3 else int(s)
        
        count = 0
        
        rem7 = 0 
        for ch in s:
            rem7 = (rem7 * 10 + int(ch)) % 7
            
        
        for ch in s:
            d = int(ch)
            
            if d == 0:
                continue
            
            if(
                d == 1 or 
                (d == 2 and last % 2 == 0) or
                (d == 3 and digit_sum % 3 == 0) or
                (d == 4 and last2 % 4 == 0) or
                (d == 5 and last in (0,5)) or
                (d == 6 and last % 2 == 0 and digit_sum % 3 == 0) or
                (d == 7 and rem7 == 0) or
                (d == 8 and last3 % 8 == 0) or
                (d == 9 and digit_sum % 9 == 0)
            ):
                count += 1
            
        return count
	
#########################################################################################
'''
https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1
'''


#########################################################################################

class Solution:
    def smallestSubstring(self, s):
        # code here
        # If any of '0','1','2' is missing, no valid substring
        if ('0' not in s) or ('1' not in s) or ('2' not in s):
            return -1
        
        zero = 0
        one = 0
        two = 0
        
        l = 0
        r = 0
        ans = -1
        
        for r in range(len(s)):
            # Count characters at right pointer
            if s[r] == '0':
                zero += 1
            elif s[r] == '1':
                one += 1
            elif s[r] == '2':
                two += 1
            
            # Shrink window from left while it contains all three
            while(zero>0 and one>0 and two>0):
                if(ans == -1):
                    ans = r-l + 1
                else:
                    ans = min(ans,(r-l+1))
                
                # Move left pointer and update counts    
                if s[l] == '0':
                    zero -= 1
                elif s[l] == '1':
                    one -= 1
                elif s[l] == '2':
                    two -= 1
                
                l += 1
        
        return ans
	
#########################################################################################
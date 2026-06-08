# Anagram
# Reversing the vowels
'''
https://www.geeksforgeeks.org/problems/anagram-1587115620/1
https://www.geeksforgeeks.org/problems/reversing-the-vowels5304/1
'''

#########################################################################################
class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        a = [0] * 26
        b = [0] * 26
       
        for i in s1:
           a[ord(i)-97] += 1
        for j in s2:
           b[ord(j)-97] += 1
        
        if a == b:
            return True
        else:
            return False
    
#########################################################################################
class Solution:
    def modify(self, s):
        # code here
        
        i = 0
        j = len(s)-1
        vow = ['a','e','i','o','u']
        a = list(s)
        
        while(i<j):
            if a[i] in vow:
                if a[j] in vow:
                   a[i],a[j] = a[j],a[i]
                   i += 1
                   j -= 1
                else:
                    j -= 1
            else:
                i += 1
                
        b = ''.join(a)   
        
        return b
    
#########################################################################################
# Check Equal Arrays
# Number of Occurrence
'''
https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
'''

#########################################################################################
class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        
        a_new = sorted(a)
        b_new = sorted(b)
        
        if a_new == b_new:
            return True
        else:
            return False
        
#########################################################################################
class Solution:
    def countFreq(self, arr, target):
        # code here
        start = 0
        end = len(arr)-1
        first_index = -1
        
        while(start<=end):
            mid = (start+end)//2
            if arr[mid] == target:
                first_index = mid
                end = mid-1
            elif arr[mid] > target:
                end = mid-1
            else:
                start = mid+1
        
        start = 0
        end = len(arr)-1
        last_index = -1
        
        while(start<=end):
            mid = (start+end)//2
            if arr[mid] == target:
                last_index = mid
                start = mid+1
            elif arr[mid] > target:
                end = mid-1
            else:
                start = mid+1
                
        result = (last_index-first_index)+1
        
        if first_index == -1:
            return 0
        else:
            return result
        
#########################################################################################
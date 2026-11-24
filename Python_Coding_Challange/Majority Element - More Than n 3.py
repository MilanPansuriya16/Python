'''
https://www.geeksforgeeks.org/problems/majority-vote/1
'''

'''
Boyer-Moore Voting Algorithm (extended version)
'''

#########################################################################################

class Solution:
    def findMajority(self, arr):
        # code here
        can1 = None
        can2 = None
        count1 = 0
        count2 = 0
        result = []
        n = len(arr)//3
        
        for nums in arr:
            if can1 == nums:
                count1 += 1
            elif can2 == nums:
                count2 += 1
            elif count1 == 0:
                can1 = nums
                count1 = 1
            elif count2 == 0:
                can2 = nums
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        
        can1_count = arr.count(can1) if count1 > 0 else 0
        can2_count = arr.count(can2) if count2 > 0 else 0
        
        
        if can1_count > n:
            result.append(can1)
        if can2_count > n:
            if can2 not in result:
                result.append(can2)
                
        result.sort()
        return result
        	
#########################################################################################
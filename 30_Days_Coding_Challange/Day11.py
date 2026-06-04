# Day 11: Peak Element and Min-Max in an Array
'''
https://www.geeksforgeeks.org/problems/peak-element/1
https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/
'''


#########################################################################################
class Solution:   
    def peakElement(self, arr):
        # Code here
        arr.insert(0,float('-inf'))
        arr.append(float('-inf'))
        
        start = 1
        end = len(arr)-1
        
        for i in range(start,end):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i
                
        return False

#########################################################################################
class Solution:
    def getMinMax(self, arr):
        # code here
        min = arr[0]
        max = arr[0]
        
        for i in arr:
            if i < min:
                min = i
            if i > max:
                max = i
        
        return [min,max]
    
#########################################################################################

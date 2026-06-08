# Two sum -Pairs with 0 Sum
# Duplicates in a Limited Range Array
'''
https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
https://www.geeksforgeeks.org/problems/find-duplicates-in-an-array/1
'''

#########################################################################################
class Solution:
    def getPairs(self, arr):
        # code here
        
        lst = []
        arr = sorted(arr)
        s = set()
        i = 0
        j = len(arr) - 1
        
        while (i < j):
            if arr[j] + arr[i] == 0:
                if (arr[i],arr[j]) in s:
                    i += 1
                    j -= 1 
                else:
                    s.add((arr[i],arr[j]))
                    lst.append([arr[i],arr[j]])
                    i += 1
                    j -= 1
            elif arr[i] + arr[j] < 0:
                i += 1
            else:
                j -= 1
        return lst
    
#########################################################################################
class Solution:
    def findDuplicates(self, arr):
        # code here
        
        dict = {}
        list = []
        
        for val in arr:
            if val in dict:
                dict[val] += 1
            else:
                dict[val] = 1
        
        for key,value in dict.items():
            if value > 1:
                list.append(key)
                
        return list
    
#########################################################################################





def firstRepeated(arr):
        # code here 
        
        dict = {}
        repeat_element = -1
        
        for i in range(len(arr)):
            if arr[i] in dict:
                repeat_element = arr[i]
            else:
                dict[arr[i]] = 1
            
        for i in range(len(arr)):
            if arr[i] == repeat_element:
                return i
        
        return -1

arr = [1,5,3,4,3,5,6]
print(firstRepeated(arr))


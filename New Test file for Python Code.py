

def binary_search(arr, k):
    start = 0
    end = len(arr)
    middle_index = len(arr)//2

    if k == arr[middle_index]:
        return True
    elif k < arr[middle_index]:
        end = middle_index 
    else:
        start = middle_index + 1
        
    for i in range(start,end):
        if arr[i] == k:
            return True
    

arr = [1,2,3,4,6]
k = 6
binary_search(arr, k)
    

# beg_index = k+1
# end_index = k
        
# arr[beg_index],arr[end_index] = arr[beg_index],arr[-end_index]
    

arr = [1, 2, 3, 4, 5, 6, 7, 8]
min = arr[0]
max = arr[0]
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i
print([min,max])
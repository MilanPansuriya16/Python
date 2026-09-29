

val = [1, 3, 0, 5, 8, 5]
wt = [2, 4, 6, 7, 9, 9]

arr = []
        
for i in range(len(val)):
    temp = [val[i],wt[i],i+1]
    arr.append(temp)

# print(arr)

arr.sort(key=lambda x: (x[1],x[0]))
print(arr)  
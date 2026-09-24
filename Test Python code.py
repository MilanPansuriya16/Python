

val = [40, 100, 120]
wt = [10, 20, 30]

arr = []
        
for i in range(len(val)):
    temp = [val[i],wt[i]]
    arr.append(temp)

print(arr)

arr.sort(key=lambda x: x[0]/x[1], reverse=True)
print(arr)  

arr = [2,3,2,3,5]
dict = {}

for i in range(1,len(arr)+1):
    dict[i] = 0

for i in arr:
    if i in dict:
        dict[i] +=1
    
lst = list(dict.values())
print(lst)
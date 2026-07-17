
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
n_freq = []
p_freq = []
for i in range(0,len(arr)):
    if arr[i] < 0:
        n_freq.append(arr[i])
    else:
        p_freq.append(arr[i])

print("Positive Frequency: ",p_freq)
print("Negative Frequency: ",n_freq)    

new_arr = []
n = len(p_freq)
m = len(n_freq)
i = 0 
j = 0
k = 0

while i < n and j < m:
    arr[k] = p_freq[i]
    arr[k+1] = n_freq[j]
    i += 1
    j += 1
    k += 2
    
while i < n:
    new_arr.append(p_freq[i])
    i += 1
    
while j < m:
    new_arr.append(n_freq[j])
    j += 1
    
            
print("New Array: ",new_arr)
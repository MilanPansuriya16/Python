nums = [1,2]
candidate = None
count = 0
m = len(nums)
if m >= 3:
    n = len(nums)//3
else:
    n = 1
arr = []
for i in range(len(nums)):
    if count == 0:
        candidate = nums[i]
        count = 1
    else:
        if candidate == nums[i]:
            count += 1
        else:
            count -= 1
    if count == n:
        if candidate not in arr:
            arr.append(candidate)
    
print(arr)

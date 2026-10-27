nums = [0,1,0,3,12]
print(nums)
n = len(nums)
i = 0
j = 0
while i < n:
    if nums[i] == 0:
        while j < n:
            if nums[j] != 0:
                break
            else:
                j += 1
    if j >= n:
        break
    nums[i],nums[j] = nums[j],nums[i]
    i += 1
    j = i

print(nums)
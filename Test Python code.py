
def subarraySum(arr, target):
    # code here
    
    l = 0
    r = 0
    sum = 0
    
    for r in range(len(arr)):
        sum += arr[r]
        
        while(sum>target):
            sum -= arr[l]
            l += 1

        if sum == target:
            return [l+1,r+1]
        
    return -1

ans = subarraySum([1,2,3,7,5], 12)
print(ans)

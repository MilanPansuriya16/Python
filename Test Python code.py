
arr = list(map(int, input().split()))
stack = []
n = len(arr)

for i in range(0,n):
    curr = arr[i]

    # A collision is possible only when the last stored value and the current value move in opposite directions.
    while stack and stack[-1] * curr < 0:
        if abs(stack[-1]) < abs(curr):
            stack.pop()
        elif abs(stack[-1]) == abs(curr):
            # Both destroy each other, so nothing is added.
            stack.pop()
            curr = None
            break
        else: # abs(stack[-1]) > abs(curr)
            # The current value is destroyed by a larger one in the stack.
            curr = None
            break
        
    if curr is not None:
        stack.append(curr)

print(stack)

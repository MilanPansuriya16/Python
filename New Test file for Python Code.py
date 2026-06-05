# beg_index = k+1
# end_index = k
        
# arr[beg_index],arr[end_index] = arr[beg_index],arr[-end_index]
def getAlternates(self, arr):
    alternate = []
    for i in range(len(arr)):
        if i % 2 == 0:
            continue
        else:
            alternate.append(arr[i])
    return alternate
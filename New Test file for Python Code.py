tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)
result = []

for i in range(len(tuple1)):
    result.append(tuple1[i] ** tuple2[i])

final_tuple = tuple(result)
print(final_tuple)
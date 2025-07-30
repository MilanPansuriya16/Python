test_tuple = ([5,6],[6,7,8],[3])
result_tuple = ()

for list in test_tuple:
    result = tuple(list)
    result_tuple = result_tuple + result

print(result_tuple)

--##############################################################--
tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)
final_tuple = ()


for i in range(len(tuple1)):
        result = (tuple1[i] ** tuple2[i],)
        final_tuple = final_tuple + result

print(final_tuple)
    
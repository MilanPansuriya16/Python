# Ordered
# Immutable
# Tuple  = ()
# We can not change the elements in the tuple after creating it but we can add or extend the tuple by concatenation it with another tuple.

test_tuple = (1,2, 45, 65,32,"True","Manish",True)

print(test_tuple)
print(type(test_tuple))

# test_tuple[2] = 100 # it will give error because tuple is immutable

#-----------------------------------------------------------------#
new_tuple = (1)
print(type(new_tuple)) # it will give int because it is not a tuple

# if we have onle one element in the tuple then we have to add comma after the element to make it a tuple
new_tuple = (1,)
print(type(new_tuple)) # it will give tuple because we have added comma after the element
#-----------------------------------------------------------------#

#-----------------------------------------------------------------#
# slicing in tuple
print(test_tuple[2:5]) # it will give (45, 65, 32)
print(test_tuple[:4]) # it will give (1, 2, 45, 65)
print(test_tuple[::-1]) # it will give the reverse of the tuple

#-----------------------------------------------------------------#

# Count function in tuple
print(test_tuple.count(1)) # it will give the count of 1 in the tuple 

# Index function in tuple
print(test_tuple.index("Manish")) # it will give the index of "Manish" in the tuple, if there are multiple "Manish" in the tuple then it will give the index of first "Manish" in the tuple


###############################################################################################################################################
'''
Tuple Questions : 
1. Write a program to return entire element as a tuple which can have a list in the tuple inputs.
Ex: 
Input: test_tuple = ([5,6],[6,7,8,9],[3])
OutPut: (5,6,6,7,8,9,3)
'''

# Solution 1 :
test_tuple = ([5,6],[6,7,8,9],[3])
result = []

for i in test_tuple:
    result = result + i

result_tuple = tuple(result)
print(result_tuple)

# Solution 2 :
test_tuple = ([5,6],[6,7,8,9],[3])
result = []

for i in test_tuple:
    result.extend(i)

result_tuple = tuple(result)
print(result_tuple)

'''
2. Write a program to return the power of each element in the first tuple with the corresponding element in the second tuple and return the result in a tuple.
Ex: 
Input: tuple1 = (10,2,3,5)
       tuple2 = (3,6,4,3)
Output: (1000, 64, 81, 125)
'''

tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)
result = []

for i in range(len(tuple1)):
    result.append(tuple1[i] ** tuple2[i])

final_tuple = tuple(result)
print(final_tuple)

###############################################################################################################################################
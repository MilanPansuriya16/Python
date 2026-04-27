# Feature of set in python
# set in maths
# Methods of set in python
# Interation in set

# Set property :
# UnOrdered
# mutable
# Can not contain duplicate
# {}

set_variable = {1,2,3,2,45,65,3,4,7} 
print(set_variable)

# Methods of set in python
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.isdisjoint(set2))

# Add method
set1.add(45)
print(set1)

# Remove vs Discard
#differece between remove and discard -->remove can give error when key is not present but discard not give error if key is not present
set3 = {11,22,33,44}
set3.remove(22)
print(set3)

set3.remove(32) # it will give error because 32 is not present in the set
set3.discard(32) # it will not give error because discard method does not give error when the element is not present in the set


######################################################################################################################333
'''
1) Given Two lists, find the missing and additional values in both the lists.
Input: List1 = [1,2,3,4,5,6]
         List2 = [4,5,6,7,8]
Output: Missing values in list1 = [7,8]
        Additional values in list1 = [1,2,3]
        Missing values in list2 = [1,2,3]
        Additional values in list2 = [7,8]
'''

list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]

set1 = set(list1)
set2 = set(list2)

missing_values_in_list1 = set2.difference(set1)    # B - A
additional_values_in_list1 = set1.difference(set2) # A - B
missing_values_in_list2 = set1.difference(set2)    # A - B
additional_values_in_list2 = set2.difference(set1) # B - A

'''
2) Given three arrays, we have to find common elements in the three sorted lists using sets.
Input: ar1 = [1,5,10,20,40,80]
       ar2 = [6,7,20,80,100]
       ar3 = [3,4,15,20,30,70,80,120]
Output: [20,80]
'''

# Method 1 : using loop 
ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

final_result = []

for i in ar1:
    if i in ar2 and i in ar3:
        final_result.append(i)

print(final_result)

# Method 2 : using set
ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

set1 = set(ar1)
set2 = set(ar2)
set3 = set(ar3) 

final_result = set1.intersection(set2).intersection(set3)
print(list(final_result))
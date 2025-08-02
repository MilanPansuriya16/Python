# Set property :
# UnOrdered
# Immutable
# Can not contain duplicate


set_variable = {1,2,3,4,5,6,7,2,1}
print(set_variable)

# empty directory
newdict = {}
print(type(newdict))

# Empty set
newset = set()
print(type(newset))

#Union,Intersection,disjoint,
set_variable1 = {2,3,4,5,6}
set_veriable2 = {4,5,6,7,8}

print(set_variable1.union(set_veriable2))
print(set_variable1.intersection(set_veriable2))
print(set_variable1.isdisjoint(set_veriable2))
print(set_variable1.difference(set_veriable2))


#Other functions
set_variable.add(45)
print(set_variable)

set_variable.remove(2)
print(set_variable)

set_variable.discard(2)
print(set_variable)

#differece between remove and discard -->remove can give error when key is not present but discard not give error if key is not present
set_variable.remove(12)
print(set_variable)
set_variable.discard(12)
print(set_variable)

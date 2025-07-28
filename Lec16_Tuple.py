#Order maintain
#Immutable

name_tuple = (1,2,"Manish",True)

print(name_tuple)
print(type(name_tuple))
print(name_tuple[0:3])

if 1 in name_tuple:
    print(f"This value is present in the tuple")

#function 
print(name_tuple.count(2))
print(name_tuple.index(2))


new_tuple = (2)
print(type(new_tuple))


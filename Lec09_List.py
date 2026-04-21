# Append list into another list
# Adding Tow list   
# Accessing list using : index and negative index
# Length Method    : len(list)
# insert Method    : list.insert(index, element)
# pop Method       : list.pop(index)
# Remove Method    : list.remove(element)
# Delete the list  : del list
# Change the list value : list[index] = new_value
# Split Method     : list.split(separator)

from loguru import logger

# list slicing : List slicing is a technique to access a specific portion of the list. It is done by specifying the start index and end index of the portion we want to access. The syntax for list slicing is list[start:end]. The start index is inclusive and the end index is exclusive. If we want to access the entire list, we can use list[:]. If we want to access the portion from the start of the list to a specific index, we can use list[:end]. If we want to access the portion from a specific index to the end of the list, we can use list[start:].
labour_name = ["Jagmohan", "Rampyare", "Mohan", 500,400,600]
print(labour_name[0:3])
print(labour_name[3:])

# reverse the list
print(labour_name[::-1]) 

# list concatenation : List concatenation is the process of combining two or more lists into a single list. It is done using the + operator. The syntax for list concatenation is list1 + list2. The resulting list will contain all the elements of list1 followed by all the elements of list2.
list1 = [1,2,3]
list2 = [4,5,6]
concatenated_list = list1 + list2
print(concatenated_list)

# list concatenation using .extend() method : The .extend() method is used to add the elements of one list to the end of another list. The syntax for using the .extend() method is list1.extend(list2). The resulting list will contain all the elements of list1 followed by all the elements of list2.
list3 = [1,2,3]
list4 = [4,5,6]
list3.extend(list4)
print(list3)

# Pop method : The .pop() method is used to remove an element from the list at a specific index and return the removed element. The syntax for using the .pop() method is list.pop(index). If the index is not specified, it will remove and return the last element of the list.
labour_name = ["Jagmohan", "Rampyare", "Mohan", 500,400,600]
removed_element = labour_name.pop()
print(f"removed element is {removed_element}")

removed_specific_element = labour_name.pop(2)
print(f"removed specific element is {removed_specific_element}")

# Remove method : The .remove() method is used to remove the first occurrence of a specific element from the list. The syntax for using the .remove() method is list.remove(element). If the element is not found in the list, it will raise a ValueError.
labour_name = ["Jagmohan", "Rampyare", "Mohan", 500,400,600]
labour_name.remove("Mohan")

# Delete the list : The del statement is used to delete a list. The syntax for using the del statement is del list. After deleting the list, it will no longer be accessible and will raise a NameError if we try to access it.
labour_name1 = ["Jagmohan", "Rampyare", "Mohan", 500,400,600]
del labour_name1

# Change the list value : We can change the value of an element in the list by accessing it using its index and assigning a new value to it. The syntax for changing the list value is list[index] = new_value.
labour_name = ["Jagmohan", "Rampyare", "Mohan", 500,400,600]
labour_name[2] = "Sohan"
labour_name[0:3] = ["Ram","Rampyare","Sohan"]
print(labour_name)

# Split Method : The .split() method is used to split a string into a list of substrings based on a specified separator. The syntax for using the .split() method is string.split(separator). If the separator is not specified, it will split the string based on whitespace.
sentence = "Hello World, Welcome to Python Programming"
split_sentence = sentence.split(' ')
print(split_sentence)

# sort method : The .sort() method is used to sort the elements of a list in ascending order. The syntax for using the .sort() method is list.sort(). If we want to sort the list in descending order, we can use the reverse parameter as list.sort(reverse=True).
numbers = [5,2,9,1,5,6] 
numbers.sort()
print(numbers)
# list : List is a collection of same or different data types. it. It is ordered collection of items which means the items in the list are stored in a specific order and we can access them using their index. The index starts from 0. We can also have negative indexing in the list which means we can access the items from the end of the list. The last item in the list has an index of -1, the second last item has an index of -2 and so on.
# Ordered (maintains the order of insertion)
# Mutable (can be changed after creation)
# [] (square brackets)
# List can contain duplicate items
# List can contain different data types
# Continues memory allocation (dynamic memory allocation)

from loguru import logger

list1 = [1,2,3,4,5]
print(list1[1])

labour_name = ["Jagmohan", "Rampyare", "Mohan", "Sohan", "Jagmohan"]
logger.info(f"First element in the list is {labour_name[0]}")

# .append() method is used to add an element at the end of the list
labour_name.append("Ram")  
logger.info(f"List after appending a new element is {labour_name}")

# .insert() method is used to add an element at a specific index in the list
labour_name.insert(0,"Ram") 
logger.info(f"List after inserting a new element at index 0 is {labour_name}")

# .extend() method is used to add multiple elements at the end of the list
new_labour = ["Ramesh","Suresh"]
labour_name.extend(new_labour) 
logger.info(f"List after extending with a new list is {labour_name}")

# negetive indexing 
logger.info(f"Last element in the list is {labour_name[-1]}")

# MultiDimensional list and how to access the elements in the multi dimensional list
labour_with_cost = [["Mahesh",500],["Ramesh",600]]
print(labour_with_cost[0][1])
print(labour_with_cost[0])

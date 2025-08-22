

'''
List
- Mutable: Yes
- Ordered: Yes
- Can contain duplicate: Yes
- Iterable: Yes

Tuple
- Mutable: No
- Ordered: Yes
- Can contain duplicate: Yes
- Iterable: Yes

Dictionary
- Mutable: Yes
- Ordered: No (Note: As of Python 3.7+, dictionaries are insertion ordered)
- Can contain duplicate: No (Keys must be unique)
- Iterable: Yes

Set
- Mutable: Yes
- Ordered: No
- Can contain duplicate: No
- Iterable: Yes
'''


# ...existing code...
'''
### Dictionary Questions

**Q1. What is dictionary in Python?**
A dictionary in Python is an unordered (in Python versions before 3.7) collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, a dictionary holds a key:value pair.

**Q2. Is dictionary mutable?**
Yes, dictionaries are mutable. You can add, remove, and change key-value pairs after the dictionary has been created.

**Q3. Can we use a tuple as a key in a dictionary?**
Yes, a tuple can be used as a key in a dictionary because tuples are immutable. Dictionary keys must be of an immutable type.
We can use a tuple, string, or int as a key in a dictionary but can not use a list as a key because keys must be immutable. So, valid keys are tuple, string, and int.

**Q4. Difference between `list.pop()` and `dictionary.pop()`?**
- `list.pop(index)`: Removes and returns the item at the specified index. If no index is provided, it removes and returns the last item in the list.
- `dictionary.pop(key)`: Removes the item with the specified key and returns its value. It requires a key as an argument and will raise a `KeyError` if the key is not found (unless a default value is provided).

**Q5. How to get all the keys available in a dictionary?**
You can use the `.keys()` method, which returns a view object containing all the keys in the dictionary.
```python
my_dict = {'a': 1, 'b': 2}
print(my_dict.keys())  # Output: dict_keys(['a', 'b'])
```

### List Questions

**Q6. Is a list mutable?**
Yes, lists are mutable. You can change their content by adding, removing, or modifying elements.

**Q7. Is a list ordered?**
Yes, lists are ordered. The items in a list maintain a specific order, and this order will be preserved.

**Q8. What is "list index out of range"?**
This is an `IndexError` that occurs when you try to access an element of a list using an index that does not exist. For example, trying to get the 5th element of a list that only has 3 elements.

**Q9. How to get the last element of a list?**
You can use a negative index of `-1`.
```python
my_list = [10, 20, 30]
last_element = my_list[-1] # 30
```

**Q10. How does list comprehension work?**
List comprehension provides a concise way to create lists. It consists of an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result is a new list created by evaluating the expression for each item in the iterable.
```python
# Example: Create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print(squares) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```


### Tuple Questions

**Q11. Is a tuple mutable?**
No, tuples are immutable. Once a tuple is created, you cannot change, add, or remove elements.

**Q12. Is a tuple ordered?**
Yes, tuples are ordered. The items have a defined order, and that order will not change.

**Q13. How to access an element of a tuple?**
You can access tuple elements by referring to the index number, inside square brackets.
```python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1]) # Output: banana
```

**Q14. How to add an element in a tuple?**
Since tuples are immutable, you cannot add items to them directly. You have to create a new tuple by concatenating the existing tuple with another tuple containing the new item(s).
```python
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4,)
print(my_tuple) # Output: (1, 2, 3, 4)
```

**Q15. How to reverse the items of a tuple?**
You can use slicing to create a new tuple with the elements in reverse order.
```python
my_tuple = (1, 2, 3, 4)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple) # Output: (4, 3, 2, 1)
```

### Set Questions

**Q16. Is a set mutable?**
Yes, sets are mutable. You can add and remove items from a set using methods like `add()` and `remove()`.

**Q17. Is a set ordered?**
No, sets are unordered collections. The items in a set do not have a defined order, and their order is not guaranteed to be preserved.

**Q18. If a list is converted into a set, will the order be maintained?**
No, the order will not be maintained. When a list is converted to a set, the resulting set will be unordered. Additionally, any duplicate elements from the list will be removed.
```python
my_list = [1, 5, 2, 4, 2, 5]
my_set = set(my_list)
print(my_set) # Output could be {1, 2, 4, 5} - order is not guaranteed.
```

// ...existing code...
my_list = [1, 5, 2, 4, 2, 5]
my_set = set(my_list)
print(my_set) # Output could be {1, 2, 4, 5} - order is not guaranteed.


**Q19. Will a set contain all the elements of a list if it is created using a list?**
No, not necessarily. A set only stores unique elements. If the original list contains duplicate values, those duplicates will be removed when the set is created. The set will contain all the *unique* elements from the list.

**Q20. What is the difference between...**
*   **List and Tuple?**
    *   **Mutability:** Lists are mutable (can be changed). Tuples are immutable (cannot be changed).
    *   **Syntax:** Lists are created with square brackets `[]`. Tuples are created with parentheses `()`.

*   **List and Set?**
    *   **Order:** Lists are ordered collections. Sets are unordered.
    *   **Duplicates:** Lists can contain duplicate elements. Sets cannot.
    *   **Indexing:** List elements can be accessed via an index. Set elements cannot.

*   **Set and Dictionary?**
    *   **Storage:** Sets store individual, unique elements. Dictionaries store key-value pairs.
    *   **Syntax:** Sets are created with `{}` or `set()`. Dictionaries are also created with `{}` but require key-value pairs (e.g., `{'key': 'value'}`). An empty `{}` creates a dictionary, not a set.

*   **Tuple and Set?**
    *   **Mutability:** Tuples are immutable. Sets are mutable.
    *   **Order:** Tuples are ordered. Sets are unordered.
    *   **Duplicates:** Tuples can contain duplicate elements. Sets cannot.

// ...existing code...

'''
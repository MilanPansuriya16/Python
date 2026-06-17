# What is Numpy?
# --> NumPy stands for Numerical Python and is used for handling large, multi-dimensional arrays and matrices. 
# --> Unlike Python's built-in lists NumPy arrays provide efficient storage and faster processing for numerical and scientific computations.

# Types of Array
# 1. One Dimensional Array: stores elements in a single row. It is the simplest type of NumPy array and is commonly used to represent a sequence of values.

import numpy as np

# a = [1, 2, 3, 4]
# arr = np.array(a)

# print("List: ", a)
# print("Numpy Array:", arr)
# print(type(a))
# print(type(arr))

# 2. Multi-Dimensional Array: stores data in two or more dimensions. The most common type is a two-dimensional array, which organizes data into rows and columns.

# l1 = [1, 2, 3, 4]
# l2 = [5, 6, 7, 8]
# l3 = [9, 10, 11, 12]
# arr = np.array([l1, l2, l3])
# print(arr)
# print(arr.shapre)

########################################################################################################

# Attribute
# 1. Shape: indicates the number of elements along each dimension. It is returned as a tuple.
# arr = np.array([ [0, 4, 2],
#                  [3, 4, 5],
#                  [23, 4, 5],
#                  [2, 34, 5],
#                  [5, 6, 7] ])
# print(arr.shape)
# output = (5,3)

# 2. Data Type (dtype): property specifies the type of data stored in an array, such as integers, floating-point numbers, or strings.
# arr1 = np.array([[0, 4, 2]])
# arr2 = np.array([0.2, 0.4, 2.4])

# print("Data type of array 1:", arr1.dtype)
# print("Data type of array 2:", arr2.dtype)

########################################################################################################

# Different Ways of Creating Numpy Array
# 1. numpy.array(): creates a NumPy array from Python sequences such as lists or tuples.
# arr = np.array([3, 4, 5, 5])
# print(arr)

# 2. numpy.fromiter(): creates a one-dimensional array from an iterable object.
# text = "Geeksforgeeks"
# arr = np.fromiter(text, dtype="U2")
# print(arr)

# # 3. numpy.arange(): returns evenly spaced values within a specified range.
# arr = np.arange(0, 20, 2, dtype=np.float32)
# print(arr)

# # 4. numpy.linspace(): returns a specified number of evenly spaced values between two limits.
# arr = np.linspace(3.5, 10, 3, dtype=np.int32)
# print(arr)

# # 5. numpy.empty(): creates an array of a given shape without initializing its values.
# arr = np.empty((4, 3), dtype=np.int32)
# print(arr)

# # 6. numpy.ones(): creates an array filled with ones.
# arr = np.ones((4, 3), dtype=np.int32)
# print(arr)

# # 7. numpy.zeros(): creates an array filled with zeros.
# arr = np.zeros((4, 3), dtype=np.int32)
# print(arr)

########################################################################################################3
'''

Create Python Numpy Arrays Using Random Number Generation
-->NumPy provides functions to create arrays filled with random numbers.

np.random.rand(): Creates an array of specified shape and fills it with random values sampled from a uniform distribution over [0, 1).
np.random.randn(): Creates an array of specified shape and fills it with random values sampled from a standard normal distribution.
np.random.randint(): Creates an array of specified shape and fills it with random integers within a given range.

'''

ar = np.random.rand(2, 3)
an = np.random.randn(2, 2)
ai = np.random.randint(1, 10, size=(2, 3))  

print(ar)
print(an)
print(ai)

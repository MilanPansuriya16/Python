import numpy as np

# 1. Accessing Elements in 1D Arrays
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])

# 2. Accessing Elements in Multidimensional Arrays
matrix = np.array([  [1, 2, 3]
                   , [4, 5, 6]
                   , [7, 8, 9]  ])

print(matrix[1, 2]) # Output = 6

# We can access elements by specifying row, column and depth indices like matrix[depth, row, column].
cube = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 
                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]]])

print(cube[1, 2, 0])       # Output = 16

###########################################################################################################################
# Slicing Arrays

# Slicing 1D Arrays: For a 1D array, slicing returns a subset of elements between the start and stop indices.
arr = np.array([0, 1, 2, 3, 4, 5])
print(arr[1:4])         # Output = [1 2 3]

# Slicing Multidimensional Arrays: In this slicing can be applied to each dimension separately which allows us to extract submatrices or smaller blocks of data.
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0:2, 1:3])

###########################################################################################################################
# Boolean Indexing

arr = np.array([10, 15, 20, 25, 30])
print(arr[arr > 20])
print(arr[(arr > 10) & (arr < 30)])

###########################################################################################################################
# Fancy Indexing

arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])        # Output: [10 30 50]

###########################################################################################################################
# Integer Array Indexing

arr = np.array([1, 2, 3, 4, 5])
print(arr[[0, 2, 4]])       # Output: [1 3 5]

###########################################################################################################################
# Using np.newaxis to Add New Dimensions

arr = np.array([1, 2, 3])
print(arr[:, np.newaxis])

###########################################################################################################################
# Modifying Array Elements

arr = np.array([1, 2, 3, 4])
arr[1:3] = 99
print(arr)

###########################################################################################################################
# In 2D Array
# Example 1: Accessing the First and Last row of a 2D NumPy array

arr = np.array([[10, 20, 30], [40, 5, 66], [70, 88, 94]])
print("Array:")
print(arr)

res = arr[[0,2]]
print("Accessed Rows :")
print(res)

# Example 2: Accessing the Middle row of 2D NumPy array

arr = np.array([[101, 20, 3, 10], [40, 5, 66, 7], [70, 88, 9, 141]])
print("Array:")
print(arr)

res = arr[1]
print("Accessed Row :")
print(res)

# Example 3: Accessing Specific Rows and Columns of a 2D NumPy array
arr = np.array([[12, 15, 18], 
                [25, 30, 35], 
                [40, 45, 50]])
print("Array:")
print(arr)

res = arr[:2, :2]   # first 2 rows, first 2 columns
print("Accessed Elements:")
print(res)

###########################################################################################################################

# In 3D Arrays
# Example 1: Accessing the Middle rows of 3D NumPy array

arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]], [[50, 65, 8], [70, 85, 10], [11, 22, 33]]])
print("Array:")
print(arr)

res = arr[:,[1]]
print("Accessed Rows:")
print(res)

# Example 2: Accessing the First and Last rows of 3D NumPy array

arr = np.array([[[10, 25, 70], [30, 45, 55], [20, 45, 7]], 
                 [[50, 65, 8], [70, 85, 10], [11, 22, 33]],
                 [[19, 69, 36], [1, 5, 24], [4, 20, 96]]])
print("Array:")
print(arr)

res = arr[:,[0, 2]]
print("Accessed Rows:")
print(res)

# Example 3: Accessing Specific Rows and Columns in a 3D NumPy array

arr = np.array([
    [[5, 10, 15], [20, 25, 30], [35, 40, 45]],
    [[2,  4,  6], [ 8, 10, 12], [14, 16, 18]],
    [[7, 14, 21], [28, 35, 42], [49, 56, 63]]
])
print("Array:")
print(arr)

res = arr[:, :2, :2]   # first 2 rows and first 2 columns from each 2D slice
print("Accessed Elements:")
print(res)

###########################################################################################################################
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

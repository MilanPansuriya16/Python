# ***numpy.stack() in Python***
# -->The numpy.stack() function is used to join multiple arrays by creating a new axis in the output array. 

# Example: This example stacks two 1D arrays along a new axis to form a 2D array.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# print(np.stack((a, b), axis=0))
# print(np.stack((a, b), axis=1))
# print(np.stack((a, b), axis=-1))


# Example 2: This example stacks two 2D arrays along axis 0, 1, and 2 to show how the new 3D structure changes.

x = np.array([[1, 2, 3],
              [4, 5, 6]])

y = np.array([[7, 8, 9],
              [10, 11, 12]])

print(np.stack((x, y), axis=0))
print(np.stack((x, y), axis=1))
print(np.stack((x, y), axis=2))


#####################################################################################################################################################3
# ***Splitting Arrays in NumPy***
# -->Splitting arrays means dividing a single NumPy array into multiple smaller sub-arrays. 

# Example: This example splits a 1D array into three smaller parts using np.array_split().

arr = np.array([1, 2, 3, 4, 5, 6])
res = np.array_split(arr, 3)
print(res)

# Splitting Methods

# 1. numpy.split()
# -->numpy.split() is used to divide an array into equal-sized subarrays. The number of splits must perfectly divide the size of the array along the chosen axis. 
# If equal division is not possible, NumPy will raise an error.

arr = np.arange(6)
res = np.split(arr, 2)
print(res)


# 2. numpy.array_split()
# -->numpy.array_split() works like split(), but it allows uneven splitting. This is useful when the array size does not divide evenly by the number of splits. NumPy will distribute the extra elements automatically.
arr = np.arange(13)
res = np.array_split(arr, 4)
print(res)

# 3. numpy.vsplit()
# -->numpy.vsplit() performs vertical splitting, meaning it divides a matrix row-wise (along axis=0). It works only on arrays with 2 or more dimensions.

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
res = np.vsplit(arr, 2)
print(res)

# 4. numpy.hsplit()
# -->numpy.hsplit() performs horizontal splitting, which divides the array column-wise (axis=1). This is helpful when separating feature columns in datasets.

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
res = np.hsplit(arr, 2)
print(res)

# 5. numpy.dsplit()
# numpy.dsplit() is used for 3D arrays. It splits the array along the third axis (axis=2). This is useful when working with stacked matrices, images, or multi-channel data.

arr = np.arange(24).reshape((2, 3, 4))
res = np.dsplit(arr, 2)
print(res)

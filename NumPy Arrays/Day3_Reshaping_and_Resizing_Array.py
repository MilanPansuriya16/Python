import numpy as np

####################################################### Reshaping #######################################################

# Example 1: This example converts a 1-D array into a 2-D array by specifying rows and columns that match the total number of elements.
a = np.array([1, 2, 3, 4, 5, 6])
r = a.reshape(2, 3)
print(r)

# Example 2: This example creates a 3-D array by grouping the original elements into blocks, each containing equal-sized 2-D sections.
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
r = a.reshape(2, 2, 2)
print(r)

# Example 3: This example demonstrates the use of -1 when one dimension is unknown. NumPy calculates that missing dimension automatically.
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
r = a.reshape(3, -1)
print(r)

####################################################### Resize #######################################################

# Example 1: This example resizes a 1D array of 6 elements into a 2×3 array. No values need repetition or truncation.
arr = np.array([1, 2, 3, 4, 5, 6])
arr.resize((2, 3))
print(arr)

# Example 2: This example resizes a 6-element array into a 3×4 shape (12 elements needed). NumPy repeats the array elements to fill the new size.
arr = np.array([1, 2, 3, 4, 5, 6])
arr.resize((3, 4))
print(arr)

# Example 3: This example resizes an array into a 2×2 shape. Since fewer elements are required, the extra values are removed.
arr = np.array([10, 20, 30, 40, 50])
arr.resize((2, 2))
print(arr)

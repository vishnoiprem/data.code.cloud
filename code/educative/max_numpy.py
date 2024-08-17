import numpy as np

arr = np.array([[1, 5, 2], [8, 3, 7], [4, 6, 9]])

# Find the index of the maximum value in the entire array
max_index_flattened = np.argmax(arr)
print("Index of max value (flattened):", max_index_flattened)

# Find the indices of maximum values along each column
max_indices_columns = np.argmax(arr, axis=0)
print("Indices of max values along columns:", max_indices_columns)

# Find the indices of maximum values along each row
max_indices_rows = np.argmax(arr, axis=1)
print("Indices of max values along rows:", max_indices_rows)
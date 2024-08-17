import numpy as np

arr = np.array([[1, 5, 2], [8, 3, 7], [4, 6, 9]])

# Find the index of the maximum value in the entire array
max_index_flattened = np.argmax(arr)
# print("Index of max value (flattened):", max_index_flattened)

# Find the indices of maximum values along each column
max_indices_columns = np.argmax(arr, axis=0)
# print("Indices of max values along columns:", max_indices_columns)

# Find the indices of maximum values along each row
max_indices_rows = np.argmax(arr, axis=1)
# print("Indices of max values along rows:", max_indices_rows)


import numpy as np

arr = np.array([[1, 5, 2], [8, 3, 7], [4, 6, 9]])

# Find the index of the minimum value in the entire array
min_index_flattened = np.argmin(arr)
# print("Index of min value (flattened):", min_index_flattened)

# Find the indices of minimum values along each column
min_indices_columns = np.argmin(arr, axis=0)
# print("Indices of min values along columns:", min_indices_columns)

# Find the indices of minimum values along each row
min_indices_rows = np.argmin(arr, axis=1)
# print("Indices of min values along rows:", min_indices_rows)




import numpy as np

arr = np.array([[3, 1, 2], [6, 4, 5], [9, 8, 7]])

# Sort the entire array (flatten and sort)
sorted_arr_flattened = np.sort(arr, axis=None)
print("Sorted flattened array:", sorted_arr_flattened)

# Sort along the first axis (sort each column)
sorted_arr_columns = np.sort(arr, axis=0)
print("Array sorted along columns:\n", sorted_arr_columns)

# Sort along the last axis (sort each row)
sorted_arr_rows = np.sort(arr, axis=1)
print("Array sorted along rows:\n", sorted_arr_rows)
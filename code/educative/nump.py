# import numpy as np
#
# print("****** np.array_split Usage ******\n")
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print("Splitting {} as \n".format(a))
# print(np.array_split(a, 3))
# print("\n")
#
# print("****** np.column_stack Usage ******\n")
# x = np.array([1,2,3])
# y = np.array([4,5,6])
# z = np.array([7,8,9])
# print("Stacking the 3 below \n")
# print(x)
# print(y)
# print(z)
# print("\n")
# print("Result is \n")
# print(np.column_stack((x,y,z)))
# print("\n")
#
# print("****** np.concatenate Usage ******\n")
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])
# print("Concatenating the 2 below along the column axis\n")
# print(a)
# print(b)
# print("\n")
# print("Result is \n")
# print(np.concatenate((a, b), axis=0))
# print("\n")
#
# print("****** np.hsplit Usage ******\n")
# x = np.arange(16.0).reshape(4, 4)
# print("Making 2 Horizontal splits(column wise) of below array \n")
# print(x)
# print("\n")
# print("Result is \n")
# print(np.hsplit(x, 2))
# print("\n")
#
# print("****** np.hstack Usage ******\n")
# a = np.array([[1],[2],[3]])
# b = np.array([[2],[3],[4]])
# print("Stacking the below 2 horizontally (column wise) \n")
# print(a)
# print(b)
# print("\n")
# print("Result is \n")
# print(np.hstack((a,b)))
# print("\n")
#
#
# print("****** np.squeeze Usage ******\n")
# x = np.array([[[0], [1], [2]]])
# print("Before Squeezing \n")
# print("x : {}\n".format(x))
# print("Shape of x : {}".format(x.shape))
# print("\n")
# print("After squeezing \n")
# print("x : {}\n".format(np.squeeze(x)))
# print("Shape of x : {}".format(np.squeeze(x).shape))
# print("\n")
#
# print("****** np.vsplit Usage ******\n")
# x = np.arange(16.0).reshape(4, 4)
# print("Making 2 Vertical splits(row wise) of below array \n")
# print(x)
# print("\n")
# print("Result is \n")
# print(np.vsplit(x, 2))
# print("\n")
#
# print("****** np.vstack Usage ******\n")
# a = np.array([[1],[2],[3]])
# b = np.array([[2],[3],[4]])
# print("Stacking the below 2 vertically (row wise) \n")
# print(a)
# print(b)
# print("\n")
# print("Result is \n")
# print(np.vstack((a,b)))
# print("\n")


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
# Split the array into 3 parts
split_arr = np.array_split(arr, 8)
# print(split_arr)

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.column_stack((a, b))
# print(c)

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis=0)
# print(c)


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
split_arr = np.hsplit(arr, 3)
# print(split_arr)


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.hstack((a, b))
# print(c)



import numpy as np

arr = np.array([[[0], [1], [2]]])
squeezed_arr = np.squeeze(arr)
# print(squeezed_arr)


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
split_arr = np.vsplit(arr, 3)
# print(split_arr)

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))
print(c)



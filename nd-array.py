import numpy as np

# 2 - Dimensional Array
two_dim_array = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim_array)

# 1 - Dimensional Array
one_dim_array = np.array([1, 2, 3, 4, 5, 6])
print(one_dim_array)

# multidimensional array
multi_dim_array = np.reshape(one_dim_array, (2, 3))
print(multi_dim_array)

print(multi_dim_array.ndim)  # number of dimensions
print(multi_dim_array.shape)  # shape of the array
print(multi_dim_array.size)  # total number of elements      
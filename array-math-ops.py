import numpy as np

arr_1 = np.array([2, 4, 6])
arr_2 = np.array([1, 3, 5])

addition = arr_1 + arr_2

subtraction = arr_1 - arr_2

multiplication = arr_1 * arr_2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)   

# broadcasting example
vector = np.array([1, 2, 3])
print(vector * 1.6)

# Indexing and slicing
a = np.array([10, 20, 30, 40, 50])
print(a[2]) 

two_dim_array = np.array([[1, 2, 3], [4, 5, 6]])
print(two_dim_array[0,2])  # This line will print the element at row 1, column 2


print("Sliced Array", a[1:4])

print(a[:3])  # This line will print the first three elements of the array  

print(a[::2])  # This line will print every second element of the array

print(a[2:])

# Stacking

a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

print("Vertical Stack:\n", np.vstack((a1, a2)))
print("Horizontal Stack:\n", np.hstack((a1, a2)))
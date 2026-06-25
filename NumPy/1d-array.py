import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)

b = np.arange(3)
print(b)

c = np.arange(1, 20, 3)
print(c)

lin_space_array = np.linspace(0, 100, 5)
print(lin_space_array)

lin_space_array_int = np.linspace(0, 100, 5, dtype=int)
print(lin_space_array_int)

char_array = np.array(['Welcome to the Math for ML'])
print(char_array)
print(char_array.dtype)

print(np.ones(5))
print(np.zeros(5))
print(np.empty(5))
print(np.random.rand(5))


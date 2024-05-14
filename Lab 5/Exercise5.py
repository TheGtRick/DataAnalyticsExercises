import numpy as np
x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89]) 
y = np.array([21, 7, 3, 45, 10, 29, 55, 4, 37, 18])
print(np.where(x > y))
print(np.where(x == y))
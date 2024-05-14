import numpy as np
array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
array = array.reshape(array.size // 3, 3)
print(array)
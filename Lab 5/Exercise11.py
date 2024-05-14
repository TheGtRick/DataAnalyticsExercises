import numpy as np
a = np.array([7,2,10,2,7,4,9,4,9,8])
b = a[a > 2]
print(b[b < 9])
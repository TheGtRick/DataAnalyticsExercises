import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
a = np.stack((a, b), axis=0).reshape(4,-1)
print(a)
import numpy as np
a = np.array([7,2,10,2,7,4,9,4,9,8])
a = (a-np.min(a))/(np.max(a)-np.min(a))
print(a)
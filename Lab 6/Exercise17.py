import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
print(np.average(df['YrSold']))
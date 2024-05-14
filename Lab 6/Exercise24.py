import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
df2 = df[df['MiscVal'] == df['PoolArea']]
print(df2)
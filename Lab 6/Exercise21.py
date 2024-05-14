import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
one_hot = pd.get_dummies(df['MSZoning'])
df = df.join(one_hot)
print(df)
import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
df = df.loc[df['SaleType'] == 'WD']
print(df)
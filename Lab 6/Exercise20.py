import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
for i in df.select_dtypes(include='number'):
    df[i] = df[i].fillna(np.mean(df[i]))
print(df)
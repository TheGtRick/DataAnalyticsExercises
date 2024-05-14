import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
df2 = df.select_dtypes(include='number').corr()
print(df2)
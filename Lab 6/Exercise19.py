import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
print(df.isna().sum())
print(f"{df.isna().sum().idxmax()}: {df[df.isna().sum().idxmax()].isna().sum()}")
import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
value_counts = df.stack().value_counts()
print(value_counts)
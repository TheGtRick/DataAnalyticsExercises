import numpy as np
import pandas as pd
df = pd.read_csv('Lab 6\\train.csv')
df['LotArea'] = (df['LotArea'] - np.min(df['LotArea'])) / (np.max(df['LotArea']) - np.min(df['LotArea']))
print(df['LotArea'])
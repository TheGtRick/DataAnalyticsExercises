import pandas as pd
import numpy as np
dataset = pd.read_csv('Lab 5\\train.csv')
print(np.mean(dataset['SalePrice']))
print(np.median(dataset['SalePrice']))
print(np.std(dataset['SalePrice']))

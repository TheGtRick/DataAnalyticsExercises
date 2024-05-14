import pandas as pd
dataset = pd.read_csv('Lab 5\\train.csv')
dataset['LotAreaVersion2'] = dataset['LotArea'] * 2
print(dataset['LotAreaVersion2'])
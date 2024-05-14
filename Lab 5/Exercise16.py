import pandas as pd
dataset = pd.read_csv('Lab 5\\train.csv')
print(dataset['LotArea'].corr(dataset['SalePrice']))
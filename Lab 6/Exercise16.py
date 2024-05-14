import numpy as np
import pandas as pd
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 6\\train.csv")
print(df[df['SalePrice'] == np.max(df['SalePrice'])])
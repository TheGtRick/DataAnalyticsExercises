import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1 = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
df2 = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
df1 = pd.get_dummies(df1, columns=['sex', 'address_type', 'school_support'])
df2 = pd.get_dummies(df2, columns=['sex', 'address_type', 'school_support'])
print(df1, df2)
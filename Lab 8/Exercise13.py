import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1 = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
df2 = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
columns = ['absences', 'age', 'health']
mins = df1[columns].min()
maxs = df1[columns].max()
df1[columns] = (df1[columns] - mins) / (maxs - mins)
mins = df2[columns].min()
maxs = df2[columns].max()
df2[columns] = (df2[columns] - mins) / (maxs - mins)
print(df1, df2)
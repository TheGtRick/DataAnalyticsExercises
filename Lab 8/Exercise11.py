import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1 = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
df2 = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
nums1 = df1.select_dtypes(include=np.number).columns
df1[nums1] = df1[nums1].fillna(df1[nums1].mean())
nums2 = df2.select_dtypes(include=np.number).columns
df1[nums2] = df2[nums2].fillna(df2[nums2].mean())
print(df1)
print(df2)
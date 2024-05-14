import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy import stats
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
print(math_students[['age', 'absences']])
print(portuguese_students[['age', 'absences']])
def handle_outliers(df, column):
    z_scores = stats.zscore(df[column])
    threshold = 2
    median_value = np.median(df[column])
    df[column] = np.where(z_scores > threshold, median_value, df[column])
handle_outliers(math_students, 'absences')
handle_outliers(math_students, 'age')
handle_outliers(portuguese_students, 'absences')
handle_outliers(portuguese_students, 'age')
print(math_students[['age', 'absences']])
print(portuguese_students[['age', 'absences']])
import pandas as pd
from sklearn.model_selection import train_test_split
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
train_portuguese, test_portuguese = train_test_split(portuguese_students)
train_math, test_math = train_test_split(math_students)
print(train_portuguese)
print(test_portuguese)
print(train_math)
print(test_math)
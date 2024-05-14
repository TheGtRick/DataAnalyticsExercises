import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
math_students['subject'] = 'math'
portuguese_students['subject'] = 'portuguese'
merged_students = pd.concat([math_students, portuguese_students], ignore_index=True)
print(merged_students)
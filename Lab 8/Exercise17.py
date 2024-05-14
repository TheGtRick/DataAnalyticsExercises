import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
math_students['subject'] = 'math'
portuguese_students['subject'] = 'portuguese'
combined_students = pd.concat([math_students, portuguese_students], ignore_index=True)
columns_to_drop = ['guardian', 'romantic_relationship', 'nursery_school','weekday_alcohol', 'weekend_alcohol']
combined_students = combined_students.drop(columns=columns_to_drop)
print(combined_students)
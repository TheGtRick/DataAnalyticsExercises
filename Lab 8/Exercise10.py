import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
scatter_math = math_students.groupby(['study_time'])['class_failures'].mean().reset_index()
scatter_portuguese = portuguese_students.groupby(['study_time'])['class_failures'].mean().reset_index()
fig, ax = plt.subplots()
ax.scatter(scatter_math['study_time'], scatter_math['class_failures'], color='b', label='Math')
ax.scatter(scatter_portuguese['study_time'], scatter_portuguese['class_failures'], color='r', label='Portuguese')
ax.set_xlabel('Study Time')
ax.set_ylabel('Failures')
plt.tight_layout()
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
math_students.boxplot(column='final_grade', by='study_time', ax=axs[0])
axs[0].set_xlabel('Study Time')
axs[0].set_ylabel('Grades')
axs[0].set_title('Math Students')
portuguese_students.boxplot(column='final_grade', by='study_time', ax=axs[1])
axs[1].set_xlabel('Study Time')
axs[1].set_ylabel('Grades')
axs[1].set_title('Portuguese Students')
plt.tight_layout()
plt.show()
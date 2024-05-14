import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
absences_math = math_students['absences']
absences_portuguese = portuguese_students['absences']
grades_math = math_students['final_grade']
grades_portuguese = portuguese_students['final_grade']
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].scatter(absences_math, grades_math, color="skyblue")
axs[0].set_xlabel('Absences')
axs[0].set_ylabel('Grades')
axs[0].set_title('Math Students')
axs[1].scatter(absences_portuguese, grades_portuguese, color="salmon")
axs[1].set_xlabel('Absences')
axs[1].set_ylabel('Grades')
axs[1].set_title('Portuguese Students')
plt.tight_layout()
plt.show()
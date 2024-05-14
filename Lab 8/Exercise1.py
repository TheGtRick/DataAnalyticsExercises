import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
ages_math = math_students['age']
ages_portuguese = portuguese_students['age']

fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].hist(ages_math, bins=10, color='skyblue', edgecolor='black')
axs[0].set_title('Age Distribution - Math School')
axs[0].set_xlabel('Age')
axs[0].set_ylabel('Frequency')

axs[1].hist(ages_portuguese, bins=10, color='salmon', edgecolor='black')
axs[1].set_title('Age Distribution - Portuguese School')
axs[1].set_xlabel('Age')
axs[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
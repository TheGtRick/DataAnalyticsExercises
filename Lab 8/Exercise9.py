import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
correlation_math = math_students.select_dtypes(include=np.number).corr()
correlation_portuguese = portuguese_students.select_dtypes(include=np.number).corr()
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
sns.heatmap(correlation_math, ax=axs[0])
axs[0].set_title('Math Students')
sns.heatmap(correlation_portuguese, ax=axs[1])
axs[1].set_title('Portuguese Students')
plt.tight_layout()
plt.show()
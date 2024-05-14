import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
gender_math = math_students["sex"]
gender_portuguese = portuguese_students["sex"]
labels = ["Math", "Portuguese"]
x = np.arange(len(labels))
width = 0.1
female = [len(gender_math[gender_math == "F"]), len(gender_portuguese[gender_portuguese == "F"])]
male = [len(gender_math[gender_math == "M"]), len(gender_portuguese[gender_portuguese == "M"])]
fig, axs = plt.subplots()
rect1 = axs.bar(x - width, male, width, color="skyblue", label="M")
rect2 = axs.bar(x + width, female, width, color="salmon", label="F")
axs.set_ylabel('Count')
axs.set_title('Gender Distribution')
axs.set_xticks(x, labels)
axs.legend()
axs.bar_label(rect1, padding=3)
axs.bar_label(rect2, padding=3)
fig.tight_layout()
plt.show()
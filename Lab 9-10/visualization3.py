import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\changed.csv")
survived_counts = df['Survived'].value_counts()
survived_counts.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Survival Distribution')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()
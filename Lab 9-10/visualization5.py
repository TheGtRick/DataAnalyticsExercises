import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\changed.csv")
sex_counts = df['Sex'].value_counts()
sex_counts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'salmon'])
plt.title('Gender Distribution')
plt.show()
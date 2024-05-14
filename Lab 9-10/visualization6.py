import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\changed.csv")
sns.pairplot(df[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']])
plt.suptitle('Pairplot of Numerical Variables', y=1.02)
plt.show()
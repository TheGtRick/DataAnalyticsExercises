import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\changed.csv")
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival Count by Gender')
plt.show()
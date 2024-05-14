import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import random
df1 = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\train.csv")
df2 = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\test.csv")
df3 = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\gender_submission.csv")
df2["Survived"] = df3["Survived"]
df = pd.concat([df1, df2])
df["Age"] = df["Age"].fillna(int(np.mean(df["Age"])))
df["Sex"] = df["Sex"].replace({'male': 0, 'female': 1})
df["Embarked"] = df["Embarked"].replace({"S": 1, "Q": 2, "C": 3})
df["Pclass"] = df["Pclass"].fillna(int(np.mean(df["Pclass"])))
df["SibSp"] = df["SibSp"].fillna(int(np.mean(df["SibSp"])))
df["Parch"] = df["Parch"].fillna(int(np.mean(df["Parch"])))
df["Fare"] = df["Fare"].fillna(np.mean(df["Fare"]))
df["Embarked"] = df["Embarked"].fillna(int(np.mean(df["Embarked"])))
df["Cabin"] = df["Cabin"].fillna(random.choice(np.array(df[df["Cabin"].notnull()]["Cabin"])))
scaler = MinMaxScaler()
df["Normalized_Fare"] = scaler.fit_transform(df[["Fare"]])
df.to_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\changed.csv", index=False)
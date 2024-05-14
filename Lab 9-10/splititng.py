import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\changed.csv")
train_df , test_df = train_test_split(df)
train_df.to_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\splited_train.csv")
test_df.to_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\splited_test.csv")
print(train_df)
print(test_df)
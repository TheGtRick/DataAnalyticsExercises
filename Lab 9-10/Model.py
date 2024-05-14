import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 9-10\\changed.csv")
df = df.select_dtypes(include="number")
other_columns = df.columns[df.columns != "Survived"]
other = df[other_columns]
x_train, x_test, y_train, y_test = train_test_split(other, df["Survived"])
model = LogisticRegression(verbose=1, max_iter=2000)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
class_report = classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Confusion Matrix:{confusion_matrix(y_test, y_pred)}")
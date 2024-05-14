import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1 = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
df2 = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
def value(x):
    if x == '2 to 5 hours':
        x = 2.5
    elif x == '5 to 10 hours':
        x = 7.5
    elif x == '<2 hours':
        x = 2
    elif x == '<10 hours':
        x = 10
    elif x == '<15 min.':
        x = 0.25
    elif x == '15 to 30 min.':
        x = 0.5
    elif x == '30 min. to 1 hour':
        x = 0.75
    else:
        x = 1
df1["Total_Time"] = df1["study_time"].apply(value) + df1["travel_time"].apply(value)
df2["Total_Time"] = df2["study_time"].apply(value) + df2["travel_time"].apply(value)
import pandas as pd
target_variable = 'class_failures'
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
print(math_students['class_failures'])
#grouped_math_students = math_students.groupby('class_failures')
#separate_dfs = [group for _, group in grouped_math_students]
#for i, separate_df in enumerate(separate_dfs):
#    print(f"DataFrame for class_failures = {i}:\n{separate_df}\n")
minority_class = math_students['class_failures'].value_counts().idxmin()
class_counts = math_students['class_failures'].value_counts()
max_class_count = class_counts.max()
indices_to_remove = []
for class_label, count in class_counts.items():
    if class_label != minority_class:
        indices = math_students[math_students['class_failures'] == class_label].index
        indices_to_remove.extend(indices[:count - max_class_count])
balanced_math_students = math_students.drop(indices_to_remove)
print(balanced_math_students)
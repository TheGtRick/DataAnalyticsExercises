import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
math_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_math_clean.csv')
portuguese_students = pd.read_csv('C:\\Users\\Rakon\\Desktop\\DataAnalytics\\Lab 8\\student_portuguese_clean.csv')
addresses_math = math_students['address_type']
addresses_portuguese = portuguese_students['address_type']

fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].pie([len(addresses_math[addresses_math == "Urban"]), len(addresses_math[addresses_math == "Rural"])], labels=['Urban', 'Rural'], explode=[0, 0.1], shadow=True)
axs[0].set_title('Address Types - Math Students')
axs[1].pie([len(addresses_portuguese[addresses_portuguese == "Urban"]), len(addresses_portuguese[addresses_portuguese == "Rural"])], labels=['Urban', 'Rural'], explode=[0, 0.1], shadow=True)
axs[1].set_title('Address Types - Portuguese Students')
plt.tight_layout()
plt.show()
import pandas as pd
import numpy as np
dataset = pd.read_csv('Lab 5\\train.csv')
dataset['LotFrontage'] = (dataset['LotFrontage'] - np.min(dataset['LotFrontage'])) / (np.max(dataset['LotFrontage']) - np.min(dataset['LotFrontage']))
dataset = dataset.rename(columns={'LotFrontage' : 'NormalizedLotFrontage'})
print(dataset['NormalizedLotFrontage'])
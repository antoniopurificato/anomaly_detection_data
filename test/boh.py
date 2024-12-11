import pandas as pd
import numpy as np
import os

df = pd.read_csv(os.getcwd() + '/../gold_test/gold_test.csv')
n = len(df)
df['Anomaly'] = np.random.choice([0, 1], size=n, p=[0.6, 0.4])
df.to_csv(os.getcwd() + '/../gold_test/gold_test_2.csv', index=False)

import pandas as pd
import math
import numpy as np

df = pd.read_csv('vaputra.csv')
print(df.to_string()) 

## Histogram
hist = df.hist(bins=3)
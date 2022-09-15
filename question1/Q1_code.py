import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

tb1 = pd.read_csv('C:\\Users\\Admin\\Desktop\\interim project\\table1.1.csv')
print(tb1)

plt.bar(tb1.CountryRegionCode, tb1.Revenue)
plt.xlabel('Country Code')
plt.ylabel('Revenue')

plt.show()
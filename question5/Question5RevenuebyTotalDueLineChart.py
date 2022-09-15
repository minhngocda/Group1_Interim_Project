import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#td means trading duration vs revenue
td = pd.read_csv("datasets/Question5_table_Revenue_by_totalDue.csv")
print(td.head())

#What is the relationship between Trading Store Duration and Revenue ?

td.plot(kind="Hist",x="Trading Duration Store", y="Revenue")
plt.title("Trading Store Duration vs Revenue")
plt.xlabel("Trading Store Duration In Years")
plt.ylabel("Revenue Value in Money ")
plt.show()
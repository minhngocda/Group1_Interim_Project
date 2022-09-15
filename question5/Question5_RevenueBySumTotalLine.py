import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#td means trading duration vs revenue
td = pd.read_csv("datasets/Question5_Revenuebysumlinetotal.csv")
print(td.head())

td["Revenue"] = td["Revenue"].apply(lambda x: x/10000)
#What is the relationship between Trading Store Duration and Revenue ?
#plt.bar(td.Duration, td.Revenue)

plt.scatter(td.Duration, td.Revenue)
plt.title("Trading Store Duration vs Revenue in Bilions$")
plt.xlabel("Trading Store Duration In Years")
plt.ylabel("Revenue Value in Money ")
plt.show()
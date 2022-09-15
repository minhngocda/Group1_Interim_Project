import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#td means trading duration vs revenue
td = pd.read_csv("datasets/Question5_table_Revenue_by_totalDue.csv")
print(td.head())

plt.scatter(td.Duration, td.Revenue)
plt.title("Trading Store Duration vs Revenue in Bilions$")
plt.xlabel("Trading Store Duration In Years")
plt.ylabel("Revenue Value in Money ")
plt.show()

#What is the relationship between Trading Store Duration and Revenue ?
#plt.bar(td.Duration, td.Revenue)
#plt.barh (td.Duration, td.Revenue)
#plt.hist (td.Duration) 
#plt.hist (td.Duration)
#plt.title("Trading Store Duration vs Revenue")
#plt.xlabel("Trading Store Duration In Years")
#plt.ylabel("Revenue Value in Money ")
#plt.show()

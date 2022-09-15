import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#We can download, use the results from SQL SERVER to create charts 

vacation_vs_bonus = pd.read_csv("datasets/Question2Bonus.csv")
#print(vacation_vs_bonus.head())
print(vacation_vs_bonus)

#What is the relationship between annual leave taken and bonus ?
plt.scatter(vacation_vs_bonus.VacationHours, vacation_vs_bonus.Bonus)
# vacation_vs_bonus.plot(kind='scatter',y='VacationHours',x='Rate')
plt.title("VacationHours_Vs_Bonus")
plt.xlabel("VacationHours")
plt.ylabel("Bonus")
plt.show()


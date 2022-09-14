import pandas as pd
import numpy as np
from matplotlib import pyplot as plt



#Pandas loadas our data
#We can download, use the results from SQL SERVER to create charts 

vacation_vs_bonus = pd.read_csv("datasets/Question2.csv")
#print(vacation_vs_bonus.head())

#What is the relationship between annual leave taken and bonus ?
plt.scatter(vacation_vs_bonus.VacationHours, vacation_vs_bonus.Rate)
# vacation_vs_bonus.plot(kind='scatter',y='VacationHours',x='Rate')
plt.xlabel("Vacation Hours(anual leave)")
plt.ylabel("Rate(bonus)")
plt.show()

#pandas imported, aliased as pd
import pandas as pd 
import numpy as np

#pandas loads the csv file 'jobtitlesickleave'
JTSL = pd.read_csv(r'C:\Users\User\Documents\CSV Python Files\QuestionFourV2.csv')
print(JTSL.head())

#matplotlib plots the data
import matplotlib.pyplot as plt

plt.bar(JTSL.PersonType, JTSL.AverageSickLeaveHours, color='b')

plt.xlabel('Person Type') #x-axis label
plt.ylabel('Average Sick Leave Taken (Hours)') #y-axis label
plt.title('What is the Relationship between Sick Leave Hours and Job Title (Person Type)') #adding a title to the chart
plt.xticks(['EM', 'SP'], 
            ['Employee', 'Sales Person']) #changing the ticks on the x-axis 

plt.show() #displays the chart


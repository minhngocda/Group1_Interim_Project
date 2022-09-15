#Import CSV file containing the data, pandas and matplotlib
import pandas
from matplotlib import pyplot as plt
Project = pandas.read_csv('Countries with higher revenue.csv')

plt.bar(Project.CountryRegionCode, Project.Revenue)

#Title
plt.title('Revenue by country') 

#Labels
plt.ylabel('Revenue in millions')
plt.xlabel('Country Code')
plt.show()
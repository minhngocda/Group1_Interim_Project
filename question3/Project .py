#Import CSV file containing the data, pandas and matplotlib
import pandas
from matplotlib import pyplot as plt
Project = pandas.read_csv('C:\\Users\\edson\\OneDrive\\Documentos\\Project Generation\\Countries with higher revenue.csv')

plt.scatter(Project.CountryRegionCode, Project.Revenue)

plt.ylabel('Revenue')
plt.xlabel('Country Code')
plt.show()
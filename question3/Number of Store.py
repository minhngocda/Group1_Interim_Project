#Import CSV file containing the data, pandas and matplotlib
import pandas
from matplotlib import pyplot as plt
Project2 = pandas.read_csv('Number of store by country.csv')

#Data
plt.bar(Project2.CountryRegionName, Project2.NumberOfStore)

#Title
plt.title('Number of Store') 

#Labels
plt.ylabel('Number of Store')
plt.xlabel('Country')
plt.show()
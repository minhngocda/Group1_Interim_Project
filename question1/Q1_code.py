import pandas as pd
from matplotlib import pyplot as plt

#import database as dataframe
tb1 = pd.read_csv('C:\\Users\\Admin\\Desktop\\interim project\\table1.1.csv')
#print(tb1)
#draw bar char using Country Region Code and Revenue
plt.bar(tb1.CountryRegionCode, tb1.Revenue)
#Set x label, y label and title for the chart
plt.xlabel('Country Code')
plt.ylabel('Revenue (*10 million USD)')
plt.title('Country Revenue')
#Show the chart
plt.show()
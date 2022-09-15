import pandas as pd
from matplotlib import pyplot as plt

#import CSV file as a dataframe tb1
tb1 = pd.read_csv('C:\\Users\\Admin\\Desktop\\interim project\\question6.csv')

#create scatter plot with x axis is Number of Employees, y axis is Store Size and size of dot represent Revenue
plt.scatter(tb1.NumberEmployees, tb1.SquareFeet, s = tb1.Revenue/1000000, alpha = 0.4)

# Add label for x, y, and tittle
plt.xlabel('Number of Employees')
plt.ylabel('Store size (square feet)')
plt.title("Relationship between Store Size, Number of Employees and Revenue")
#Show the chart
plt.show()

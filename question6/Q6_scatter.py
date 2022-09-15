import pandas as pd
from matplotlib import pyplot as plt

tb1 = pd.read_csv('C:\\Users\\Admin\\Desktop\\interim project\\question6.csv')
print(tb1.info())


plt.scatter(tb1.NumberEmployees, tb1.SquareFeet, s = tb1.Revenue/1000000, alpha = 0.4)
plt.xlabel('Number of Employees')
plt.ylabel('Store size (square feet)')
plt.title("Relationship between Store Size, Number of Employees and Revenue")
plt.show()
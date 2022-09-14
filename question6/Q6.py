#import data from excel onto python
import pandas
exampletable = pandas.read_csv('C:\\Users\\User\\Documents\\Interim Project\\Question6.csv')
print(exampletable.head())

#create a graph
from matplotlib import pyplot as plt
plt.plot(exampletable.annualrevenue, exampletable.numberofemployees, exampletable.storesize_ft)
plt.scatter(exampletable.annualrevenue.x, exampletable.numberofemployees.x, exampletable.storesize_ft.x. figures.y)

plt.title("The relationship between the size of the stores, number of employees and revenue")
plt.ylabel('Figure')
plt.xlabel('numberofemployees')('annualrevenue')('storesize_ft')

plt.legend()
plt.show()

DRAFT

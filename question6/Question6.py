import pandas
from matplotlib import pyplot as plt
t = pandas.read_csv('C:\\Users\\User\\Documents\\Interim Project\\Question6.csv')
print(t.head())

fig, ax1 = plt.subplots()
ax1.plot(t.NumberOfEmployees, color='red', label = "Employees")
ax1.plot(t.AnnualRevenue, color='blue', label = "Revenue")
plt.style.use('seaborn')

ax1.set_title("The relationship between the size of the stores, number of employees and revenue")
ax1.set_ylabel("StoreSize_ft")
ax1.set_xlabel("NumberOfEmployees / AnnualRevenue")

fig.tight_layout()
plt.legend()
plt.show()

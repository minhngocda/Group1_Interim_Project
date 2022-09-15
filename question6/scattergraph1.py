import pandas
from matplotlib import pyplot as plt
t = pandas.read_csv('C:\\Users\\User\\Documents\\Interim Project\\Question6.csv')
print(t.head())

t = t.groupby([t.StoreSize_ft],as_index=False).mean()
print(t.head())

x=t.StoreSize_ft
y=t.AnnualRevenue
z=t.NumberOfEmployees

fig, ax1 = plt.subplots()
plt.style.use('seaborn')
ax1.set_title("The relationship between the size of the stores and number of employees")
ax1.set_ylabel("StoreSize_ft")
ax1.set_xlabel("Number Of Employees")

plt.scatter(x,z)
plt.show()
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
ax1.set_title("The relationship between the size of the stores and number of revenue")
ax1.set_ylabel("StoreSize_ft")
ax1.set_xlabel("Annual Revenue")

plt.scatter(x,y)
plt.show()

#scatter graph 2
ax1.set_title("The relationship between the annual revenue and number of revenue")
ax1.set_ylabel("NumberOfEmployees")
ax1.set_xlabel("Annual Revenue")

plt.scatter(y,z)
plt.show()

#scatter graph 3
ax1.set_title("The relationship between the annual revenue and number of revenue")
ax1.set_ylabel("AnnualRevenue")
ax1.set_xlabel("NumberOfEmployees")

plt.scatter(z,t)
plt.show()

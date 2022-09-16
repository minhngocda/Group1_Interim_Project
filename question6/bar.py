import pandas 
import numpy
from matplotlib import pyplot as plt
t = pandas.read_csv('C:\\Users\\User\\Documents\\Interim Project\\Question6.csv')
print(t.head())

conditions = [(t.StoreSize_ft < 20000), (t.StoreSize_ft < 40000),(t.StoreSize_ft < 60000),(t.StoreSize_ft > 60000)]
storelabels = ['small(20)','medium(40)','big(60)','very big']

t['size'] = numpy.select(conditions, storelabels)
print(t)

t = t.groupby('size', as_index=False).mean()
print(t.head())

plt.bar(t.size, t.NumberOfEmployees)
plt.show()
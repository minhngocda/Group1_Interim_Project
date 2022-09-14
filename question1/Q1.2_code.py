import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

tb1 = pd.read_csv('C:\\Users\\Admin\\Desktop\\interim project\\table1.2.csv')
print(tb1)

#data
#x-axis
region = tb1.Region
#y-axis
y1 = tb1.SalesYTD
y2 = tb1.SalesLastYear
 
#bar chart properties
x = np.arange(len(region))
width = 0.3
 
#draw grouped bar chart
fig, ax = plt.subplots()
bar1 = ax.bar(x - width/2, y1, width, label='SalesYTD')
bar2 = ax.bar(x + width/2, y2, width, label='SalesLastYear')
 
#ax.set_xlabel('Year')
ax.set_ylabel('USD')
ax.set_title('Total Sales per Region in United States')
ax.set_xticks(x, region)
ax.legend()
 
 
#fig.tight_layout()
 
plt.show()
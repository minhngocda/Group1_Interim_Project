import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

OLSL = pd.read_csv(r'C:\Users\User\Documents\CSV Python Files\OLvsSL.csv')
print(OLSL.head())

plt.bar(OLSL.OrganizationLevel, OLSL.AverageSickLeaveHours)

plt.xlabel('Organization Level')
plt.ylabel('Average Sick Leave Taken (Hours)')
plt.title('Average Sick Leave Taken by Organization Level')
plt.xticks([1.0, 2.0, 3.0, 4.0],
            ['Level 1', 'Level 2', 'Level 3', 'Level 4'])

plt.show()
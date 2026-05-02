import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('copy1.xlsx')

angle = data['Angle']
Counts = data['Counting Rate']

plt.yscale('log')
plt.plot(angle, Counts, color = 'red')
plt.xlabel('Angle (degrees)')
plt.ylabel('Counting rate (cps)')


plt.show()
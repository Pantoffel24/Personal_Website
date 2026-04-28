import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

SodiumData = pd.read_csv('sodium.csv',sep = ';')

#print(SodiumData.dtypes)
x_axis = pd.to_numeric(SodiumData['Angle (rad) Run #1'])
y_axis = pd.to_numeric(SodiumData['Light Intensity (%) Run #1'])

plt.plot(x_axis,y_axis, color = 'green')


plt.xlabel('Angle (degrees)')
plt.ylabel('Light intensity (%)')

plt.grid()
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

HydrogenData = pd.read_csv('hydrogen.csv',sep = ';')


x_axis = pd.to_numeric(HydrogenData['Angle (rad) Run #1'])
y_axis = pd.to_numeric(HydrogenData['Light Intensity (%) Run #1'])

plt.plot(x_axis,y_axis, color = 'purple')


plt.xlabel('Angle (degrees)')
plt.ylabel('Light intensity (%)')

plt.grid()
plt.show()
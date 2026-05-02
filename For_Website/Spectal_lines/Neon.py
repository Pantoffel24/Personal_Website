import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

NeonData = pd.read_csv('Neon.csv',sep = ';')


x_axis = pd.to_numeric(NeonData['Angle (rad) Run #1'])
y_axis = pd.to_numeric(NeonData['Light Intensity (%) Run #1'])

plt.plot(x_axis,y_axis,color = 'blue')


plt.xlabel('Angle (degrees)')
plt.ylabel('Light intensity (%)')

plt.grid()
plt.show()
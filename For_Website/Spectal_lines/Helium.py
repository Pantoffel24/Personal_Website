import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

HeliumData = pd.read_csv('helium.csv',sep = ';')


x_axis = pd.to_numeric(HeliumData['Angle (rad) Run #1'])
y_axis = pd.to_numeric(HeliumData['Light Intensity (%) Run #1'])

plt.plot(x_axis,y_axis,color = 'red')


plt.xlabel('Angle (degrees)')
plt.ylabel('Light intensity (%)')

plt.grid()
plt.show()
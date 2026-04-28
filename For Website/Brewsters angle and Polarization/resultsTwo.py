import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('p2.csv',sep = ';')

LightIntensity = data['Light Intensity (%) Run #1']
Angle = data['Angle. Ch 1+2 (rad) Run #1']

plt.plot(Angle, LightIntensity, color = 'blue')

plt.grid()
plt.xlabel("Angel (rads)")
plt.ylabel("Light intesity (%)")
plt.show()
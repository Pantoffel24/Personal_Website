import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('p3.csv',sep = ';')

LightIntensity = data['Light Intensity (%) Run #2']
Angle = data['Angle. Ch 3+4 (rad) Run #2']

plt.plot(Angle, LightIntensity, color = 'brown')

plt.grid()
plt.xlabel("Angel (rads)")
plt.ylabel("Light intesity (%)")
plt.show()
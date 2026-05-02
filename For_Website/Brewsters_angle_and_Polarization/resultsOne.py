import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('p2.3_final.csv',sep = ';')

LightIntensity = data['Light Intensity (%) Run #1']
Angle = data['Angle. Ch 3+4 (rad) Run #1']

plt.plot(Angle, LightIntensity, color = 'red')

plt.grid()
plt.xlabel("Angel (rads)")
plt.ylabel("Light intesity (%)")
plt.show()
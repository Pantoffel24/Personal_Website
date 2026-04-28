import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('Double slit 0.5.csv',sep = ';')

position = data['Position (m) Run #1']
intensity = data['Light Intensity (%) Run #1']

plt.plot(position,intensity,color = 'purple')
plt.show()
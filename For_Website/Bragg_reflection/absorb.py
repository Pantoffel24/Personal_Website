import matplotlib.pyplot as plt
import pandas as pd

thickness = [0, 0.084, 0.168, 0.252, 0.336, 0.420, 0.504, 0.588]
xray = [0.777, 0.086, 0.018, 0.064, 0.025, 0.009, 0.003, 0.001]

plt.plot(thickness, xray, color = 'red')

plt.title('Thickness of Aluminium')
plt.xlabel('Al Thicnkess (cm)')
plt.ylabel('Counts per second')
plt.show()
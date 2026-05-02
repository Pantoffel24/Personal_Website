import numpy as numpy
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

#data used for the experiment
sinTheta = [1.00, 0.98, 0.94, 0.87, 0.77]
#radius = [math.log(5), math.log(4.5), math.log(4.3), math.log(3.8), math.log(3.1)]
radius = [5, 4.5, 4.3, 3.8, 3.1]
radErr = 0.15

plt.plot(sinTheta, radius, color = 'blue')
plt.errorbar(sinTheta, radius, radErr, fmt = 'ro', capsize = 5)

plt.xlabel('Sin theta')
plt.ylabel('radius (cm)')
plt.grid('radius')

plt.show()
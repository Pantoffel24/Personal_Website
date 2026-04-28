import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_excel('copy1.xlsx')

x = np.array([0,1,2,3,4,5,6,7]).reshape(-1,1)
y = np.array([2420, 1800, 750, 320, 150, 50, 17, -20])

model = LinearRegression().fit(x,y)

coef = model.coef_
intercept = model.intercept_

x_space = np.linspace(0,7,100).reshape(-1,1)
y_pred = coef*x_space + intercept

plt.scatter(x,y,)
plt.plot(x_space, y_pred,color = 'red')
plt.xlabel('Number of aluminium plate')
plt.ylabel('Counts per second')
plt.show()

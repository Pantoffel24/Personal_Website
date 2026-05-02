import numpy as np
import matplotlib.pyplot as plt

#Constants
lam = 5
To = 0 #C (environment temp)
Ti = 50 #C (initial temp)
dt = 0.01 #s

#Arrays for storage
Temp_vals = []
t_vals = []

#Defining the formulas
def temperature(T):
    return T - lam*(T - To)*dt

#while loop to calculate values
n = 0 #counter variable
Tn = Ti #stores current velocity values
TnOne = 0 #stores new velocity values
while n<50:
    TnOne = temperature(Tn)
    print("Temperature: "+str(TnOne))
    #print("position: "+str(xnOne))
    Tn = TnOne
    Temp_vals.append(TnOne)
    n = n+1 

#Plotting t-values
for i in range(50):
    t_vals.append((i+1)*0.01)

#Matplotlib code for plotting the functions
plt.plot(t_vals, Temp_vals)

plt.grid()
plt.legend()
plt.show()
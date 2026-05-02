#Christoffel Schoeman
#38655349
#NUMMET
import numpy as np
import matplotlib.pyplot as plt

#Kinematic equations will be used

#Constants 
xi = 0 #m
vi = 1 #m/s
m = 1 #kg
a = 1 #m/s^2
dt = 0.01 #s
#Arrays to store new, needed values
x_vals = []
v_vals = []
t_vals = []

#Defining needed formulas
def veloctiy(v):
    return v + a*dt

def position(x,v):
    return x+veloctiy(v)*dt


#while loop to calculate values
n = 0 #counter variable
vn = vi #stores current velocity values
xn = xi #stores current position values
vnOne = 0 #stores new velocity values
xnOne = 0 #stores new position values
while n < 50:
    vnOne = veloctiy(vn)
    xnOne = position(xn,vn)
    #print("velocity: "+str(vnOne))
    #print("position: "+str(xnOne))
    vn = vnOne
    xn = xnOne
    v_vals.append(vnOne)
    x_vals.append(xnOne)
    n = n+1


#Plotting t-values
for i in range(50):
    t_vals.append((i+1)*0.01)

#Matplotlib code for plotting the functions
figure, axis = plt.subplots(2)

#For the displacement function
axis[0].plot(t_vals,x_vals)
axis[0].set_title("Displacement against time")

#For velocity function
axis[1].plot(t_vals,v_vals)
axis[1].set_title("Velocity against time")



plt.legend()
plt.show()
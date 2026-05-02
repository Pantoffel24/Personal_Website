import matplotlib.pyplot as plt
import pandas as pd

KosRay = pd.read_excel("KosRayData.xlsx")
years = KosRay["Year"]
intensity = KosRay["CR Proton intensity (J)"]
magneticField = KosRay["Magnetic field (nT)"]
modulationValues = KosRay["Modulation value"]
gamma = KosRay["Calculated Gamma values"]

plt.plot(
    years,
    gamma,
    color = "green"
)
plt.title('Gamma values for corresponding modulation parameter and magnetic field values, through the years 1977 to 2000', style = 'italic')
plt.grid()
plt.show()
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

sns.set_theme(style = "darkgrid")
sns.set_palette("pastel")

KosRay = pd.read_excel("KosRayData.xlsx")
years = KosRay["Year"]
intensity = KosRay["CR Proton intensity (J)"]
magneticField = KosRay["Magnetic field (nT)"]
modulationValues = KosRay["Modulation value"]

fig, axes = plt.subplots(1, 2)
sns.lineplot(
    ax = axes[0],
    data = KosRay,
    x = years,
    y = intensity,
    color = 'green'
).set_title("CR proton intensity (j) from 1977 to 2000", fontstyle = 'italic')

sns.lineplot(
    ax = axes[1],
    data = KosRay, 
    x = years, 
    y = magneticField,
    color = 'red'
).set_title("Magnetic field of the sun from 1977 to 2000", fontstyle = 'italic')

sns.lineplot(
    data = KosRay,
    x = years,
    y = modulationValues,
    color = 'orange'
).set_title('Modulation value of the given Magnetic values from the years 1977 to 2000', fontstyle = 'italic')
plt.show()


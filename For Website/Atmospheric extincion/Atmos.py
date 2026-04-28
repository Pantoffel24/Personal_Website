import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_excel("UsefulData.ods", engine="odf")

# Keep only necessary columns and drop rows with any NaNs
df = df[["Airmass", "Instrumental Magnitude"]].dropna()

# Extract variables
Airmass = df["Airmass"]
IM = df["Instrumental Magnitude"]

# Reshape Airmass for sklearn (must be 2D)
X = Airmass.values.reshape(-1, 1)
Y = IM

# Fit model
model = LinearRegression()
model.fit(X, Y)

slope = model.coef_[0]
intercept = model.intercept_
#BD124523
print(f"Extinction Coefficient (slope): {slope:.4f}")
print(f"Y-axis cut-off (intercept): {intercept:.4f}")

# Predict using the fitted model
regression_line = model.predict(X)

# Plot original data
plt.scatter(Airmass, IM, color="red", label="Data")

# Plot regression line
plt.plot(Airmass, regression_line, color="blue", label="Fit")

# Style the plot
plt.gca().invert_yaxis()
plt.xlabel("Airmass")
plt.ylabel("Instrumental Magnitude")
plt.title("Linear Regression: Atmospheric Extinction")
plt.grid()
plt.legend()
plt.show()
